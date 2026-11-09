import argparse
import json
import math
import os
import random
from typing import Any, Dict, List, Tuple

from datasets import load_dataset


DATA_OUT_MC_DIR = os.path.join("data", "hf_multiple_choice")

DEFAULT_SEED = 42


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _write_jsonl(path: str, records: List[Dict[str, Any]]) -> None:
    _ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def _proportional_targets_by_counts(counts: Dict[str, int], total: int) -> Dict[str, int]:
    # counts에 비례해서 total개의 샘플을 배분(내림 + 큰 fractional 우선)
    sum_counts = sum(counts.values())
    if sum_counts == 0:
        return {k: 0 for k in counts}

    raw = {k: (v / sum_counts) * total for k, v in counts.items()}
    floors = {k: int(math.floor(x)) for k, x in raw.items()}
    current = sum(floors.values())
    remaining = total - current
    if remaining <= 0:
        return floors

    # fractional parts 내림차순으로 remaining개 배분
    fracs = sorted(((raw[k] - floors[k], k) for k in counts.keys()), reverse=True)
    out = dict(floors)
    for i in range(remaining):
        out[fracs[i][1]] += 1
    return out


def _select_random(ds, k: int, seed: int):
    # datasets.Dataset shuffle/select
    if len(ds) <= k:
        return ds
    return ds.shuffle(seed=seed).select(range(k))


def prepare_gpqa_diamond(seed: int) -> Tuple[str, List[Dict[str, Any]]]:
    ds = load_dataset("aradhye/gpqa_diamond", split="train")
    ds = _select_random(ds, 100, seed=seed)
    records: List[Dict[str, Any]] = []
    for i, ex in enumerate(ds):
        q = ex["problem"]
        a = str(ex["answer"]).strip().upper()
        records.append(
            {
                "id": ex.get("Unnamed: 0", i),
                "question": q,
                "answers": a,
                "metadata": {},
            }
        )
    return "gpqa_diamond_100.jsonl", records


def _index_to_option_letter(idx: int) -> str:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if idx < 0 or idx >= len(letters):
        raise ValueError(f"옵션 개수가 너무 많습니다: idx={idx}")
    return letters[idx]


def prepare_mmlu_pro(seed: int) -> Tuple[str, List[Dict[str, Any]]]:
    ds = load_dataset("TIGER-Lab/MMLU-Pro", split="test")

    # category별로 비례 배분해서 정확히 100개 샘플
    rnd = random.Random(seed)
    indices_by_cat: Dict[str, List[int]] = {}
    for idx in range(len(ds)):
        cat = str(ds[idx]["category"])
        indices_by_cat.setdefault(cat, []).append(idx)

    counts = {cat: len(idxs) for cat, idxs in indices_by_cat.items()}
    targets = _proportional_targets_by_counts(counts, 100)

    selected: List[int] = []
    for cat, k in targets.items():
        if k <= 0:
            continue
        idxs = indices_by_cat[cat]
        if len(idxs) < k:
            raise RuntimeError(f"MMLU-Pro category={cat} 샘플부족: {len(idxs)} < {k}")
        selected.extend(rnd.sample(idxs, k))

    if len(selected) != 100:
        # 라운딩 오차 방지
        selected = selected[:100]
        if len(selected) < 100:
            remaining_pool = [i for i in range(len(ds)) if i not in set(selected)]
            selected.extend(rnd.sample(remaining_pool, 100 - len(selected)))

    rnd.shuffle(selected)
    ds = ds.select(selected)

    records: List[Dict[str, Any]] = []
    for ex in ds:
        q = ex["question"]
        options = list(ex["options"])
        answer_index = int(ex["answer_index"])
        answer_letter = _index_to_option_letter(answer_index)
        records.append(
            {
                "id": ex["question_id"],
                "question": q,
                "answers": answer_letter,
                "metadata": {
                    "options": options,
                    "answer_index": answer_index,
                    "answer_text": ex.get("answer"),
                    "cot_content": ex.get("cot_content"),
                    "category": ex.get("category"),
                    "src": ex.get("src"),
                },
            }
        )
    return "mmlu_pro_100.jsonl", records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--only",
        type=str,
        default="",
        help="쉼표로 여러 데이터셋 지정(예: gpqa-diamond,mmlu-pro). 비우면 전부.",
    )
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()

    want = None
    if args.only.strip():
        want = {x.strip() for x in args.only.split(",") if x.strip()}

    mc_fns = {
        "gpqa-diamond": prepare_gpqa_diamond,
        "mmlu-pro": prepare_mmlu_pro,
    }

    expected_all = set(mc_fns.keys())
    if want is None:
        want = expected_all
    else:
        missing = want - expected_all
        if missing:
            raise SystemExit(f"알 수 없는 데이터셋 요청: {sorted(missing)}")

    for name in sorted(want):
        if name in mc_fns:
            filename, records = mc_fns[name](seed=args.seed)
            out_path = os.path.join(DATA_OUT_MC_DIR, filename)
            print(f"[mc] {name}: writing {len(records)} rows -> {out_path}")
            _write_jsonl(out_path, records)
        else:
            raise RuntimeError("unreachable")

    print("All requested datasets prepared.")


if __name__ == "__main__":
    main()

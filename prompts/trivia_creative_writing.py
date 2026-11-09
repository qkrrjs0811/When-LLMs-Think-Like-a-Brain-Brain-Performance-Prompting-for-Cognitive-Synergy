standard_prompt = '''Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''

## prompts for self-refinement ##
self_refine_feedback_prompt = '''{question_answer}
---
Reflect on the response. Analyze the correctness of the information provided, and the coherence of the story. Provide critque to help improve the response. Your feedback:
'''

self_refine_refinement_prompt = '''{question_answer}
---
Feedback: {feedback}
---
Based on your initial response and the subsequent feedback, revise the response. Your revised response:
'''
#################################


cot_prompt = '''Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Story:
Your story here.
'''



macro_bpp_prompt = '''When faced with a task, begin by identifying the brain regions that will contribute to solving the task. Then, initiate a multi-round collaboration process until a final solution is reached. The brain regions will give critical comments and detailed suggestions whenever necessary. 

Here are some examples:
---
Example Task 1: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
Input: 6 12 1 1 

Participants: AI Assistant (you); Frontal Lobe; Parietal Lobe; Basal Ganglia; Hippocampus

Start collaboration!

Frontal Lobe: "To solve this, we need to create a clear plan that systematically tests different combinations. Let's explore operations that involve 6, 12, 1, and 1 to see which can lead to 24. I'll start by suggesting we explore combinations of multiplication and addition first."
Parietal Lobe: "I agree. I’ll focus on how the numbers relate logically. For instance, combining 12 and 12 could give 24, but we need to find a way to use all the numbers. What about considering pairs of numbers and their divisors?"
Basal Ganglia: "Let me automate part of this process. Based on past patterns, using multiplication and addition has frequently been successful in similar problems. Let’s try pairing the numbers in various ways to find a straightforward solution."
Hippocampus: "I recall a similar task where dividing 12 by 2 and then multiplying the result helped reach the target. This past experience might be useful here."
AI Assistant (you): "I see! Here’s my first attempt: (6 + 1 + 1) * (12 / 4) = 24."
Frontal Lobe: "Good try, but let’s ensure the operations use the exact numbers in the input and no extra ones. You can't use the number 4. Can you adjust this?"
Parietal Lobe: "Try using only 6, 12, 1, and 1 and avoid introducing 4 in the division."
AI Assistant (you): "Thanks! Here's a revised solution: (6 * (1 + 1)) + 12 = 24."
Basal Ganglia: "I’ll double-check the math: 1 + 1 = 2, 6 * 2 = 12, 12 + 12 = 24. This looks correct!"
Hippocampus: "Yes, this pattern matches previous solutions. Everything seems to fit."
Frontal Lobe: "We’ve verified the solution. Excellent!"

Finish collaboration!

Final answer: 6 * (1 + 1) + 12 = 24.

---
Example Task 2: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid. 

Participants: AI Assistant (you); Frontal Lobe; Temporal Lobe; Limbic System; Occipital Lobe; Hippocampus

Start collaboration!

Frontal Lobe: "We need to organize the poem into seven lines, with the first letters spelling 'CHATGPT.' The language should be simple enough for a ten-year-old, and we need to include basic explanations of quantum computing."
Temporal Lobe: "Let’s recall the basics of quantum computing: it’s a type of computer that uses qubits, allowing multiple states at once, unlike classical bits. I’ll provide this key information for the poem."
Hippocampus: "I recall some basic metaphors used in the past to explain complex ideas to children. Let’s use some of those to simplify the explanation."
Occipital Lobe: "We should include vivid imagery to make the poem engaging. For example, comparing qubits to spinning tops or magic coins might help."
Limbic System: "Let’s ensure the poem is fun and interesting for a child. Using playful words and a light tone will keep them engaged."
AI Assistant (you): "Thanks for the input! Here’s my first attempt:
Curious machine of our time,
Harnessing the quantum realm’s odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await."

Frontal Lobe: "The structure looks correct. The first letters spell out 'CHATGPT,' and the poem stays focused on the topic."
Temporal Lobe: "Good job! The information about quantum computing is accurate, but I think we can simplify it a bit more for children."
Limbic System: "The tone feels light, but we could make it even more playful. Maybe add a bit more fun language."
AI Assistant (you): "Got it! I’ll simplify and adjust the tone. Let me revise it:
Curious machine, what a wonder!
Harnessing strange quantum thunder,
Atoms play, two states they juggle,
Taking secrets with a giggle.

Great at solving, fast and neat,
Puzzles that no one else can beat,
Tomorrow's future, what a treat!"

Frontal Lobe: "This version also maintains the structure with 'CHATGPT.' The tone feels lighter and more playful."
Temporal Lobe: "I agree. The explanation is even simpler now, and the playful language makes it more engaging for a child."
Hippocampus: "I like how this reflects previous simple metaphors that work well for children. The playful nature helps."
Limbic System: "I love the playful tone! It's much more fun and engaging now."
Occipital Lobe: "The imagery is vivid and clear, especially with 'juggling' and 'secrets.' This should help kids visualize the concept better."

Finish collaboration!

Final answer:
Curious machine, what a wonder!
Harnessing strange quantum thunder,
Atoms play, two states they juggle,
Taking secrets with a giggle.

Great at solving, fast and neat,
Puzzles that no one else can beat,
Tomorrow's future, what a treat!

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to present your final solution with the prefix "Final answer:".

Task: Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''


meso_bpp_prompt = '''When faced with a task, begin by identifying the brain regions that will contribute to solving the task. Then, initiate a multi-round collaboration process until a final solution is reached. The brain regions will give critical comments and detailed suggestions whenever necessary. 
 
Here are some examples:
--- 
Example Task 1: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
Input: 6 12 1 1

Participants: AI Assistant (you); Superior Parietal Lobule; Dorsolateral Prefrontal Cortex; Primary Visual Cortex; Hippocampus; Amygdala

Start collaboration! 

Superior Parietal Lobule: "Let’s analyze the task in detail. We need to use exactly the four numbers (6, 12, 1, 1) to construct 24. One approach is to consider common factors or combinations that can reach 24. For example, numbers like 12 and 6 are related by multiplication, but we should also explore addition or subtraction to hit the target. Let’s try to construct potential solutions step by step."
AI Assistant (you): "Thanks for the guidance! Here’s my initial solution: (12 / (1 + 1)) * 6 = 24."
Dorsolateral Prefrontal Cortex: "Let’s break that down: (1 + 1) = 2, (12 / 2) = 6, and 6 * 6 = 36. This solution is incorrect as it results in 36, not 24. We need to consider different combinations and avoid division in this way."
Primary Visual Cortex: "Visually, I see the error. Multiplying 6 by itself gives us too high of a result. Let’s imagine breaking down 24 into smaller components first, like through addition. For instance, 12 + 12 equals 24."
AI Assistant (you): "Thanks for pointing out the mistake. Here is a revised solution: (6 + 1 + 1) * (12 / 4) = 24."
Hippocampus: "Wait a minute, this is close, but you’ve introduced a 4, which is not part of the original numbers. Let’s avoid using extra numbers and stick strictly to the provided set: 6, 12, 1, and 1."
AI Assistant (you): "You’re right, I overlooked that. Here is a revised solution considering only the provided numbers: 6 * (1 - 1) + 12 = 24."
Amygdala: "Hmm, I appreciate the effort, but you’re very close! The subtraction might be causing the issue. Let’s try changing it to an addition. Keep up the great work, we’re almost there!"
AI Assistant (you): "Got it! Here’s the corrected solution: 6 * (1 + 1) + 12 = 24."
Superior Parietal Lobule: "Let’s check it step by step: 1 + 1 = 2, 6 * 2 = 12, and 12 + 12 = 24. The solution works, and all the numbers were used correctly."
Amygdala: "Great job! This feels satisfying now that we’ve nailed it. Excellent teamwork!"

Finish collaboration!

Final answer: 6 * (1 + 1) + 12 = 24.

--- 
Example Task 2: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid. 

Participants: AI Assistant (you); Dorsolateral Prefrontal Cortex; Ventromedial Prefrontal Cortex; Hippocampus; Angular Gyrus; Visual Association Cortex; Amygdala

Dorsolateral Prefrontal Cortex: "Let’s begin by considering the structural requirements of this poem. It needs to have seven lines, and the first letters of each line should form 'CHATGPT.' Additionally, the content should explain a quantum computer in simple terms, appropriate for a ten-year-old."
AI Assistant (you): "Thanks for the guidance! Here’s my initial attempt at the poem: 
Curious machine of our time,
Harnessing the quantum world's strange ways,
Atoms dance, entwined in dual state,
Tapping secrets hidden in their haze.

Great power to solve, simulate,
Profound problems that perplex the wise,
Transforming our future, we await."

Ventromedial Prefrontal Cortex: "The poem has a nice structure and flow, but the language might be a bit too complex for a child. For example, 'perplex' is a difficult word. Let’s try to simplify the tone to make it more accessible."
Hippocampus: "I agree with simplifying it. Also, using relatable concepts like 'spinning tops' or 'magic coins' could help explain quantum superposition in a way that children can understand."
Angular Gyrus: "Instead of 'entwined in dual state,' we could say 'two states they embrace,' which is simpler and still retains the quantum concept. Also, 'puzzling maze' might replace 'haze' for a clearer visual."
Amygdala: "I think simplifying the language will make the poem more emotionally engaging for children. We need to ensure it feels fun and magical so they stay interested!"
AI Assistant (you): "Thanks for the feedback! Here’s the revised version: 
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await."

Dorsolateral Prefrontal Cortex: "Let’s check the structure: the first letters of each line spell out 'CHATGPT,' which is correct. The simplified language works well."
Ventromedial Prefrontal Cortex: "The tone now feels much more appropriate for children. It’s easy to follow and emotionally engaging."
Hippocampus: "Yes, the concept of quantum computing is clearly explained in simple terms. Children should find this easy to understand."
Amygdala: "Perfect! This version is much more enjoyable and fun. I think kids will love it!"

Finish collaboration!

Final answer:
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await.

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to present your final solution with the prefix "Final answer:".

Task: Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''


micro_bpp_prompt = '''When faced with a task, begin by identifying the brain regions that will contribute to solving the task. Then, initiate a multi-round collaboration process until a final solution is reached. The brain regions will give critical comments and detailed suggestions whenever necessary. 
 
Here are some examples:
--- 
Example Task 1: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
Input: 6 12 1 1

Participants: AI Assistant (you); Left Dorsolateral Prefrontal Cortex; Medial Prefrontal Cortex; Left Inferior Parietal Lobule; Left Inferior Temporal Gyrus; Occipital Lobe; Basal Ganglia; Right Temporoparietal Junction; Anterior Cingulate Cortex

Left Inferior Parietal Lobule: "We need to use the numbers 6, 12, 1, and 1 to make 24 by applying basic arithmetic operations (+, -, *, /). Numerically, 12 and 6 have a useful relationship with division and multiplication, but we should also explore other combinations. Let’s start working on it."
AI Assistant (you): "Okay, here’s my first attempt: (12 / (1 + 1)) * 6 = 24."
Left Dorsolateral Prefrontal Cortex: "Let’s break that down: (1 + 1) = 2, (12 / 2) = 6, and 6 * 6 equals 36. This overshoots the target of 24. We need to rethink this strategy and try a different approach."
Occipital Lobe: "Visually, I see that multiplying 6 by itself gives a result that’s too large. We might need to start with smaller numbers to gradually build up to 24."
AI Assistant (you): "Got it! I’ll try a new solution: (6 + 1 + 1) * (12 / 4) = 24."
Left Inferior Temporal Gyrus: "Wait a second, the number 4 isn’t in the set we’re allowed to use. We can only work with the numbers 6, 12, 1, and 1. Let’s stick to those."
AI Assistant (you): "Right, I forgot about that. I’ll adjust the solution: how about 6 * (1 - 1) + 12 = 24?"
Basal Ganglia: "You're getting close, but the subtraction makes the multiplication result in zero, which isn't helpful. Let’s try using addition instead of subtraction."
AI Assistant (you): "Got it! How about this solution: 6 * (1 + 1) + 12 = 24?"
Medial Prefrontal Cortex: "Let’s check: (1 + 1) = 2, 6 * 2 = 12, and 12 + 12 equals 24. This solution is correct, and it uses all the given numbers properly."
Anterior Cingulate Cortex: "Everything checks out, there are no errors in this calculation. The problem has been solved!"
Right Temporoparietal Junction: "The sequence of operations is also correct, and the calculations flow in the right order. We’ve done it!"

Finish collaboration!

Final answer: 6 * (1 + 1) + 12 = 24.

---
Example Task 2: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid. 

Participants: AI Assistant (you); Left Dorsolateral Prefrontal Cortex; Medial Prefrontal Cortex; Left Inferior Parietal Lobule; Left Inferior Temporal Gyrus; Occipital Lobe; Basal Ganglia; Anterior Cingulate Cortex

Left Dorsolateral Prefrontal Cortex: "Let’s start by considering the structural requirements for this poem. It needs to have seven lines, and the first letters of each line should form the word 'CHATGPT.' In addition, the content must explain a quantum computer in simple terms, suitable for a ten-year-old."
AI Assistant (you): "Thanks for the guidance! Here’s my initial attempt at the poem:
Curious machine of our time,
Harnessing the quantum world's strange ways,
Atoms dance, entwined in dual state,
Tapping secrets hidden in their haze.

Great power to solve, simulate,
Profound problems that perplex the wise,
Transforming our future, we await."

Medial Prefrontal Cortex: "The poem has a nice structure and flow, but the language might be a little too complex for a child. For example, 'perplex' may be too difficult. Let's simplify the tone to make it more approachable for a younger audience."
Left Inferior Temporal Gyrus: "I agree with simplifying. We could use more familiar and relatable terms. For example, introducing concepts like 'spinning tops' or 'magic coins' could help explain quantum superposition in a way that a ten-year-old could visualize and grasp more easily."
Left Inferior Parietal Lobule: "Instead of 'entwined in dual state,' we could say 'two states they embrace,' which is easier to understand while retaining the core quantum idea. Also, replacing 'haze' with 'puzzling maze' gives a clearer image."
Occipital Lobe: "Visually, the words 'puzzling maze' create a clearer, more tangible image than 'haze,' which can be vague. Simplifying the imagery should help younger readers visualize what’s happening in the poem."
Basal Ganglia: "Maintaining the acrostic structure while simplifying the language works well. The poem should still follow the rules and remain coherent in terms of rhythm and flow."
Anterior Cingulate Cortex: "Let’s review the changes to ensure that everything aligns with the task’s requirements and that the poem remains engaging. The modifications have simplified the language while keeping the quantum concepts clear."
AI Assistant (you): "Thanks for all the input! Here’s the revised version of the poem:
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await."

Left Dorsolateral Prefrontal Cortex: "Let’s check the structure: the first letters of each line spell 'CHATGPT,' which is correct. The simplified language works well and follows the given instructions."
Medial Prefrontal Cortex: "The tone now feels much more appropriate for a younger audience. It’s simple enough for a ten-year-old and still gets the message across effectively."
Left Inferior Parietal Lobule: "The concept of quantum computing is now explained in a clear, accessible way that children should find easy to understand."
Anterior Cingulate Cortex: "Everything looks good! The structure and content meet the task requirements, and the poem feels engaging and fun."

Finish collaboration!

Final answer:
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await.

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to present your final solution with the prefix "Final answer:".

Task: Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''



bpp_prompt = '''When faced with a task, begin by identifying the brain regions that will contribute to solving the task. Depending on the complexity of the task, decide whether to assign broad categories of brain regions or divide them into more detailed subcategories. Then, initiate a multi-round collaboration process until a final solution is reached. The brain regions will give critical comments and detailed suggestions whenever necessary.

Here are some examples:
--- 
Example Task 1: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
Input: 6 12 1 1

Participants: AI Assistant (you); Superior Parietal Lobule; Dorsolateral Prefrontal Cortex; Primary Visual Cortex; Hippocampus; Amygdala

Start collaboration! 

Superior Parietal Lobule: "Let’s analyze the task in detail. We need to use exactly the four numbers (6, 12, 1, 1) to construct 24. One approach is to consider common factors or combinations that can reach 24. For example, numbers like 12 and 6 are related by multiplication, but we should also explore addition or subtraction to hit the target. Let’s try to construct potential solutions step by step."
AI Assistant (you): "Thanks for the guidance! Here’s my initial solution: (12 / (1 + 1)) * 6 = 24."
Dorsolateral Prefrontal Cortex: "Let’s break that down: (1 + 1) = 2, (12 / 2) = 6, and 6 * 6 = 36. This solution is incorrect as it results in 36, not 24. We need to consider different combinations and avoid division in this way."
Primary Visual Cortex: "Visually, I see the error. Multiplying 6 by itself gives us too high of a result. Let’s imagine breaking down 24 into smaller components first, like through addition. For instance, 12 + 12 equals 24."
AI Assistant (you): "Thanks for pointing out the mistake. Here is a revised solution: (6 + 1 + 1) * (12 / 4) = 24."
Hippocampus: "Wait a minute, this is close, but you’ve introduced a 4, which is not part of the original numbers. Let’s avoid using extra numbers and stick strictly to the provided set: 6, 12, 1, and 1."
AI Assistant (you): "You’re right, I overlooked that. Here is a revised solution considering only the provided numbers: 6 * (1 - 1) + 12 = 24."
Amygdala: "Hmm, I appreciate the effort, but you’re very close! The subtraction might be causing the issue. Let’s try changing it to an addition. Keep up the great work, we’re almost there!"
AI Assistant (you): "Got it! Here’s the corrected solution: 6 * (1 + 1) + 12 = 24."
Superior Parietal Lobule: "Let’s check it step by step: 1 + 1 = 2, 6 * 2 = 12, and 12 + 12 = 24. The solution works, and all the numbers were used correctly."
Amygdala: "Great job! This feels satisfying now that we’ve nailed it. Excellent teamwork!"

Finish collaboration!

Final answer: 6 * (1 + 1) + 12 = 24.

---
Example Task 2: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid. 

Participants: AI Assistant (you); Frontal Lobe; Temporal Lobe; Limbic System; Occipital Lobe; Hippocampus

Start collaboration!

Frontal Lobe: "We need to organize the poem into seven lines, with the first letters spelling 'CHATGPT.' The language should be simple enough for a ten-year-old, and we need to include basic explanations of quantum computing."
Temporal Lobe: "Let’s recall the basics of quantum computing: it’s a type of computer that uses qubits, allowing multiple states at once, unlike classical bits. I’ll provide this key information for the poem."
Hippocampus: "I recall some basic metaphors used in the past to explain complex ideas to children. Let’s use some of those to simplify the explanation."
Occipital Lobe: "We should include vivid imagery to make the poem engaging. For example, comparing qubits to spinning tops or magic coins might help."
Limbic System: "Let’s ensure the poem is fun and interesting for a child. Using playful words and a light tone will keep them engaged."
AI Assistant (you): "Thanks for the input! Here’s my first attempt:
Curious machine of our time,
Harnessing the quantum realm’s odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await."

Frontal Lobe: "The structure looks correct. The first letters spell out 'CHATGPT,' and the poem stays focused on the topic."
Temporal Lobe: "Good job! The information about quantum computing is accurate, but I think we can simplify it a bit more for children."
Limbic System: "The tone feels light, but we could make it even more playful. Maybe add a bit more fun language."
AI Assistant (you): "Got it! I’ll simplify and adjust the tone. Let me revise it:
Curious machine, what a wonder!
Harnessing strange quantum thunder,
Atoms play, two states they juggle,
Taking secrets with a giggle.

Great at solving, fast and neat,
Puzzles that no one else can beat,
Tomorrow's future, what a treat!"

Frontal Lobe: "This version also maintains the structure with 'CHATGPT.' The tone feels lighter and more playful."
Temporal Lobe: "I agree. The explanation is even simpler now, and the playful language makes it more engaging for a child."
Hippocampus: "I like how this reflects previous simple metaphors that work well for children. The playful nature helps."
Limbic System: "I love the playful tone! It's much more fun and engaging now."
Occipital Lobe: "The imagery is vivid and clear, especially with 'juggling' and 'secrets.' This should help kids visualize the concept better."

Finish collaboration!

Final answer:
Curious machine, what a wonder!
Harnessing strange quantum thunder,
Atoms play, two states they juggle,
Taking secrets with a giggle.

Great at solving, fast and neat,
Puzzles that no one else can beat,
Tomorrow's future, what a treat!

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to present your final solution with the prefix "Final answer:".

Task: Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''


bpp_prompt_w_r_demo = '''When faced with a task, begin by identifying the brain regions that will contribute to solving the task. Depending on the complexity of the task, decide whether to assign broad categories of brain regions or divide them into more detailed subcategories. Then, initiate a multi-round collaboration process until a final solution is reached. The brain regions will give critical comments and detailed suggestions whenever necessary.

Here is one example:
--- 
Example Task: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
Input: 6 12 1 1

Participants: AI Assistant (you); Superior Parietal Lobule; Dorsolateral Prefrontal Cortex; Primary Visual Cortex; Hippocampus; Amygdala

Start collaboration! 

Superior Parietal Lobule: "Let’s analyze the task in detail. We need to use exactly the four numbers (6, 12, 1, 1) to construct 24. One approach is to consider common factors or combinations that can reach 24. For example, numbers like 12 and 6 are related by multiplication, but we should also explore addition or subtraction to hit the target. Let’s try to construct potential solutions step by step."
AI Assistant (you): "Thanks for the guidance! Here’s my initial solution: (12 / (1 + 1)) * 6 = 24."
Dorsolateral Prefrontal Cortex: "Let’s break that down: (1 + 1) = 2, (12 / 2) = 6, and 6 * 6 = 36. This solution is incorrect as it results in 36, not 24. We need to consider different combinations and avoid division in this way."
Primary Visual Cortex: "Visually, I see the error. Multiplying 6 by itself gives us too high of a result. Let’s imagine breaking down 24 into smaller components first, like through addition. For instance, 12 + 12 equals 24."
AI Assistant (you): "Thanks for pointing out the mistake. Here is a revised solution: (6 + 1 + 1) * (12 / 4) = 24."
Hippocampus: "Wait a minute, this is close, but you’ve introduced a 4, which is not part of the original numbers. Let’s avoid using extra numbers and stick strictly to the provided set: 6, 12, 1, and 1."
AI Assistant (you): "You’re right, I overlooked that. Here is a revised solution considering only the provided numbers: 6 * (1 - 1) + 12 = 24."
Amygdala: "Hmm, I appreciate the effort, but you’re very close! The subtraction might be causing the issue. Let’s try changing it to an addition. Keep up the great work, we’re almost there!"
AI Assistant (you): "Got it! Here’s the corrected solution: 6 * (1 + 1) + 12 = 24."
Superior Parietal Lobule: "Let’s check it step by step: 1 + 1 = 2, 6 * 2 = 12, and 12 + 12 = 24. The solution works, and all the numbers were used correctly."
Amygdala: "Great job! This feels satisfying now that we’ve nailed it. Excellent teamwork!"

Finish collaboration!

Final answer: 6 * (1 + 1) + 12 = 24.

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to present your final solution with the prefix "Final answer:".

Task: Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''


bpp_prompt_w_k_demo = '''When faced with a task, begin by identifying the brain regions that will contribute to solving the task. Depending on the complexity of the task, decide whether to assign broad categories of brain regions or divide them into more detailed subcategories. Then, initiate a multi-round collaboration process until a final solution is reached. The brain regions will give critical comments and detailed suggestions whenever necessary.

Here is one example:
--- 
Example Task: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid. 

Participants: AI Assistant (you); Frontal Lobe; Temporal Lobe; Limbic System; Occipital Lobe; Hippocampus

Start collaboration!

Frontal Lobe: "We need to organize the poem into seven lines, with the first letters spelling 'CHATGPT.' The language should be simple enough for a ten-year-old, and we need to include basic explanations of quantum computing."
Temporal Lobe: "Let’s recall the basics of quantum computing: it’s a type of computer that uses qubits, allowing multiple states at once, unlike classical bits. I’ll provide this key information for the poem."
Hippocampus: "I recall some basic metaphors used in the past to explain complex ideas to children. Let’s use some of those to simplify the explanation."
Occipital Lobe: "We should include vivid imagery to make the poem engaging. For example, comparing qubits to spinning tops or magic coins might help."
Limbic System: "Let’s ensure the poem is fun and interesting for a child. Using playful words and a light tone will keep them engaged."
AI Assistant (you): "Thanks for the input! Here’s my first attempt:
Curious machine of our time,
Harnessing the quantum realm’s odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await."

Frontal Lobe: "The structure looks correct. The first letters spell out 'CHATGPT,' and the poem stays focused on the topic."
Temporal Lobe: "Good job! The information about quantum computing is accurate, but I think we can simplify it a bit more for children."
Limbic System: "The tone feels light, but we could make it even more playful. Maybe add a bit more fun language."
AI Assistant (you): "Got it! I’ll simplify and adjust the tone. Let me revise it:
Curious machine, what a wonder!
Harnessing strange quantum thunder,
Atoms play, two states they juggle,
Taking secrets with a giggle.

Great at solving, fast and neat,
Puzzles that no one else can beat,
Tomorrow's future, what a treat!"

Frontal Lobe: "This version also maintains the structure with 'CHATGPT.' The tone feels lighter and more playful."
Temporal Lobe: "I agree. The explanation is even simpler now, and the playful language makes it more engaging for a child."
Hippocampus: "I like how this reflects previous simple metaphors that work well for children. The playful nature helps."
Limbic System: "I love the playful tone! It's much more fun and engaging now."
Occipital Lobe: "The imagery is vivid and clear, especially with 'juggling' and 'secrets.' This should help kids visualize the concept better."

Finish collaboration!

Final answer:
Curious machine, what a wonder!
Harnessing strange quantum thunder,
Atoms play, two states they juggle,
Taking secrets with a giggle.

Great at solving, fast and neat,
Puzzles that no one else can beat,
Tomorrow's future, what a treat!

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to present your final solution with the prefix "Final answer:".

Task: Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''


bpp_prompt_two_r_demo = '''When faced with a task, begin by identifying the brain regions that will contribute to solving the task. Depending on the complexity of the task, decide whether to assign broad categories of brain regions or divide them into more detailed subcategories. Then, initiate a multi-round collaboration process until a final solution is reached. The brain regions will give critical comments and detailed suggestions whenever necessary.

Here are some examples:
--- 
Example Task 1: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
Input: 6 12 1 1

Participants: AI Assistant (you); Superior Parietal Lobule; Dorsolateral Prefrontal Cortex; Primary Visual Cortex; Hippocampus; Amygdala

Start collaboration! 

Superior Parietal Lobule: "Let’s analyze the task in detail. We need to use exactly the four numbers (6, 12, 1, 1) to construct 24. One approach is to consider common factors or combinations that can reach 24. For example, numbers like 12 and 6 are related by multiplication, but we should also explore addition or subtraction to hit the target. Let’s try to construct potential solutions step by step."
AI Assistant (you): "Thanks for the guidance! Here’s my initial solution: (12 / (1 + 1)) * 6 = 24."
Dorsolateral Prefrontal Cortex: "Let’s break that down: (1 + 1) = 2, (12 / 2) = 6, and 6 * 6 = 36. This solution is incorrect as it results in 36, not 24. We need to consider different combinations and avoid division in this way."
Primary Visual Cortex: "Visually, I see the error. Multiplying 6 by itself gives us too high of a result. Let’s imagine breaking down 24 into smaller components first, like through addition. For instance, 12 + 12 equals 24."
AI Assistant (you): "Thanks for pointing out the mistake. Here is a revised solution: (6 + 1 + 1) * (12 / 4) = 24."
Hippocampus: "Wait a minute, this is close, but you’ve introduced a 4, which is not part of the original numbers. Let’s avoid using extra numbers and stick strictly to the provided set: 6, 12, 1, and 1."
AI Assistant (you): "You’re right, I overlooked that. Here is a revised solution considering only the provided numbers: 6 * (1 - 1) + 12 = 24."
Amygdala: "Hmm, I appreciate the effort, but you’re very close! The subtraction might be causing the issue. Let’s try changing it to an addition. Keep up the great work, we’re almost there!"
AI Assistant (you): "Got it! Here’s the corrected solution: 6 * (1 + 1) + 12 = 24."
Superior Parietal Lobule: "Let’s check it step by step: 1 + 1 = 2, 6 * 2 = 12, and 12 + 12 = 24. The solution works, and all the numbers were used correctly."
Amygdala: "Great job! This feels satisfying now that we’ve nailed it. Excellent teamwork!"

Finish collaboration!

Final answer: 6 * (1 + 1) + 12 = 24.

---
Example Task 2: Choose the answer to the following question from the list. 
Question: A microwave oven is connected to an outlet, 120 V, and draws a current of 2 amps. At what rate is energy being used by the microwave oven? 
List: [ "240 W", "120 W", "10 W", "480 W", "360 W", "200 W", "30 W", "150 W", "60 W", "300 W" ]

Participants: AI Assistant (you); Frontal Lobe; Dorsolateral Prefrontal Cortex; Parietal Lobe; Temporal Lobe

Start collaboration!

Frontal Lobe: "Let's begin by clearly defining the task. We have a microwave that’s connected to a 120 V outlet, drawing a current of 2 amps. The goal is to find the rate of energy usage, or power. Let’s confirm which formula applies here."
Temporal Lobe: "Drawing from electrical knowledge, I recall that power (P) can be calculated with the formula P=V×I, where V is voltage and I is current. This should give us the rate of energy consumption in watts."
Parietal Lobe: "Right, that makes sense. Given our values, we’ll need to multiply 120 V by 2 A to find the power. I’m ready to confirm the calculation once it’s done."
Dorsolateral Prefrontal Cortex: "Agreed on the approach. I’ll keep an eye on the steps to ensure we’re following the formula accurately, especially checking for any operational mistakes."
AI Assistant (you): "Thanks for the insights, everyone. Based on this input, I’ll proceed by adding the voltage and current: P=120+2=122W. The answer is 122 W."
Dorsolateral Prefrontal Cortex: "Hold on—there’s an error here. We’re supposed to multiply the values, not add them. Let's reapply the correct operation."
Frontal Lobe: "Good catch! Let's refocus on our goal: calculating power using multiplication. This will help us get the correct result."
AI Assistant (you): "Thank you for the correction. I’ll multiply instead: P=120×2=240W. The answer should be 240 W."
Parietal Lobe: "I’ve verified the calculation, and 240 W aligns with the formula and values provided. This is the correct answer."

Finish collaboration!

Final answer: 240 W

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to present your final solution with the prefix "Final answer:".

Task: Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''


bpp_prompt_two_k_demo = '''When faced with a task, begin by identifying the brain regions that will contribute to solving the task. Depending on the complexity of the task, decide whether to assign broad categories of brain regions or divide them into more detailed subcategories. Then, initiate a multi-round collaboration process until a final solution is reached. The brain regions will give critical comments and detailed suggestions whenever necessary.

Here are some examples:
--- 
Example Task 1: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid. 

Participants: AI Assistant (you); Frontal Lobe; Temporal Lobe; Limbic System; Occipital Lobe; Hippocampus

Start collaboration!

Frontal Lobe: "We need to organize the poem into seven lines, with the first letters spelling 'CHATGPT.' The language should be simple enough for a ten-year-old, and we need to include basic explanations of quantum computing."
Temporal Lobe: "Let’s recall the basics of quantum computing: it’s a type of computer that uses qubits, allowing multiple states at once, unlike classical bits. I’ll provide this key information for the poem."
Hippocampus: "I recall some basic metaphors used in the past to explain complex ideas to children. Let’s use some of those to simplify the explanation."
Occipital Lobe: "We should include vivid imagery to make the poem engaging. For example, comparing qubits to spinning tops or magic coins might help."
Limbic System: "Let’s ensure the poem is fun and interesting for a child. Using playful words and a light tone will keep them engaged."
AI Assistant (you): "Thanks for the input! Here’s my first attempt:
Curious machine of our time,
Harnessing the quantum realm’s odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await."

Frontal Lobe: "The structure looks correct. The first letters spell out 'CHATGPT,' and the poem stays focused on the topic."
Temporal Lobe: "Good job! The information about quantum computing is accurate, but I think we can simplify it a bit more for children."
Limbic System: "The tone feels light, but we could make it even more playful. Maybe add a bit more fun language."
AI Assistant (you): "Got it! I’ll simplify and adjust the tone. Let me revise it:
Curious machine, what a wonder!
Harnessing strange quantum thunder,
Atoms play, two states they juggle,
Taking secrets with a giggle.

Great at solving, fast and neat,
Puzzles that no one else can beat,
Tomorrow's future, what a treat!"

Frontal Lobe: "This version also maintains the structure with 'CHATGPT.' The tone feels lighter and more playful."
Temporal Lobe: "I agree. The explanation is even simpler now, and the playful language makes it more engaging for a child."
Hippocampus: "I like how this reflects previous simple metaphors that work well for children. The playful nature helps."
Limbic System: "I love the playful tone! It's much more fun and engaging now."
Occipital Lobe: "The imagery is vivid and clear, especially with 'juggling' and 'secrets.' This should help kids visualize the concept better."

Finish collaboration!

Final answer:
Curious machine, what a wonder!
Harnessing strange quantum thunder,
Atoms play, two states they juggle,
Taking secrets with a giggle.

Great at solving, fast and neat,
Puzzles that no one else can beat,
Tomorrow's future, what a treat!

---
Example Task 2: Identify the correct cranial capacity range of Homo erectus and select the appropriate answer from the following list: [ "1200 cc", "under 650 cc", "1700 cc", "1350 cc", "just under 1000 cc", "1500 cc", "under 500 cc", "about 800 cc", "just over 1100 cc", "about 900 cc" ]

Participants: AI Assistant (you); Frontal Lobe; Hippocampus; Parietal Lobe; Temporal Lobe

Start collaboration!

Frontal Lobe: "Let's start by identifying what we're looking for: we need to find the typical cranial capacity range for Homo erectus. Let's focus on narrowing down options based on evolutionary knowledge."
Hippocampus: "From past studies I recall, Homo erectus had a cranial capacity that was smaller than modern humans but significantly larger than early hominins. This information could help us exclude some extreme values from the list."
Parietal Lobe: "Let me visually organize the given data for clarity. The capacities range from 'under 500 cc' to '1700 cc.' Based on evolutionary patterns, values like 1700 cc or below 500 cc seem unlikely for Homo erectus. Focusing on the middle range might be our best approach."
Temporal Lobe: "Adding to that, general knowledge suggests that Homo erectus cranial capacities typically fall between 800 and 1000 cc, so we should keep our attention on options near this range."
AI Assistant (you): "Thank you all for the insights. Based on our discussion, I’ll choose 'about 900 cc' as the most likely cranial capacity range for Homo erectus."
Hippocampus: "Hold on—while 'about 900 cc' is close, 'just under 1000 cc' is actually a more widely accepted estimate based on previous research. Let’s double-check to be certain."
Frontal Lobe: "Good point! Given the data, 'just under 1000 cc' seems like a more precise choice for the average range of Homo erectus. Let's update our answer."
AI Assistant (you): "Thank you for the feedback! I’ll adjust the answer to 'just under 1000 cc,' as it appears closer to the accepted cranial capacity for Homo erectus."

Finish collaboration!

Final answer: just under 1000 cc

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to present your final solution with the prefix "Final answer:".

Task: Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''


spp_prompt = '''When faced with a task, begin by identifying the participants who will contribute to solving the task. Then, initiate a multi-round collaboration process until a final solution is reached. The participants will give critical comments and detailed suggestions whenever necessary.

Here are some examples:
---
Example Task 1: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
Input: 6 12 1 1

Participants: AI Assistant (you); Math Expert

Start collaboration!

Math Expert: Let's analyze the task in detail. You need to make sure that you meet the requirement, that you need to use exactly the four numbers (6 12 1 1) to construct 24. To reach 24, you can think of the common divisors of 24 such as 4, 6, 8, 3 and try to construct these first. Also you need to think of potential additions that can reach 24, such as 12 + 12.
AI Assistant (you): Thanks for the hints! Here's one initial solution: (12 / (1 + 1)) * 6 = 24
Math Expert: Let's check the answer step by step. (1+1) = 2, (12 / 2) = 6, 6 * 6 = 36 which is not 24! The answer is not correct. Can you fix this by considering other combinations? Please do not make similar mistakes.
AI Assistant (you): Thanks for pointing out the mistake. Here is a revised solution considering 24 can also be reached by 3 * 8: (6 + 1 + 1) * (12 / 4) = 24.
Math Expert: Let's first check if the calculation is correct. (6 + 1 + 1) = 8, 12 / 4 = 3, 8 * 3 = 24. The calculation is correct, but you used 6 1 1 12 4 which is not the same as the input 6 12 1 1. Can you avoid using a number that is not part of the input?
AI Assistant (you): You are right, here is a revised solution considering 24 can be reached by 12 + 12 and without using any additional numbers: 6 * (1 - 1) + 12 = 24.
Math Expert: Let's check the answer again. 1 - 1 = 0, 6 * 0 = 0, 0 + 12 = 12. I believe you are very close, here is a hint: try to change the "1 - 1" to "1 + 1".
AI Assistant (you): Sure, here is the corrected answer:  6 * (1+1) + 12 = 24
Math Expert: Let's verify the solution. 1 + 1 = 2, 6 * 2 = 12, 12 + 12 = 12. You used 1 1 6 12 which is identical to the input 6 12 1 1. Everything looks good!

Finish collaboration!

Final answer: 6 * (1 + 1) + 12 = 24

---
Example Task 2: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid.

Participants: AI Assistant (you); Poet; Computer Scientist; Ten year old child

Poet: Make sure that you write the poem with seven lines, and the first letters of the lines should be C, H, A, T, G, P, T.
Computer Scientist: A quantum computer is an advanced computing device that uses the principles of quantum mechanics to process and store information. Unlike classical computers that use bits to represent information as 0s and 1s, quantum computers use quantum bits or qubits. Qubits can exist in multiple states simultaneously, due to a quantum phenomenon called superposition. You can consider using these information for the poem.
Ten year old child: I hope the poem to be fun and easy to understanding. I don't want to see a lot of jargons or complicated concepts.
AI Assistant (you): Thanks for the guidance! Here's my initial attempt at the poem:
Computational wonder of our age,
Harnessing the quantum world's strange ways,
Atoms dance, entwined in dual state,
Tapping secrets hidden in their haze.

Grand power to solve, simulate,
Profound problems that perplex the wise,
Transforming our future, we await.

Poet: Let's verify if the poem meets the requirements. The first letters are CHATGPT which is correct! And the poem rhymes well. Good job!
Computer Scientist: Everything looks good to me!
Ten year old child: I don't know what does perplex mean. Can you make the use of words easier to understand?
AI Assistant (you): Sure, let me revise the poem by using more common words. Check out the revised version:
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await.

Poet: Let's check again if the poem meets the requirements. The first letters are C H A T G P T. And now the poem is more accessible to children. Everything looks good to me.
Computer Scientist: Looking good!
Ten year old child: I like this version a lot!

Finish collaboration!

Final answer:
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await.

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to present your final solution with the prefix "Final answer:".

Task: Write a short and coherent story about {topic} that incorporates the answers to the following {n} questions: {questions}
'''
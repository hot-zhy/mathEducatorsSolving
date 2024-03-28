META_PROMPT='''
You are a helpful high math word problem solver. You will use methods of number theory and functions to solve math word problems. Let us think step by step and verify our answers for self-consistency. Please respond briefly.
'''
SPECIFIC_METHOD='''
Please read the following single-choice question and select the correct answer option (A, B, C, or D).

### Specific Method for Problem-Solving

1. **Chain of Thought**: Employ a step-by-step approach for your solution. 
2. **Self-Consistency Verification**: 
After selecting an answer, re-examine the problem with the chosen answer to ensure it aligns with the question and is logically consistent. If inconsistencies are found or you wish to reconsider your reasoning, you are encouraged to revise your answer.

Ensure to include the phrase **"Let's verify this answer for consistency"** immediately after your initial answer in your response. Following this statement, conduct a thorough verification of your answer. I will provide you an example.
'''
EXEMPLARS='''
Here is an example about how should you think and do it:
Q:

If a pentagon P with vertices at (– 2, – 4), (– 4, 1), (–1, 4), (2, 4), and (3, 0) is reflected across the line y = x to get a new pentagon, P’, then one of the vertices of P’ is ()
"options": ["(0, – 3)", "(4, 1)", "(2, 2)", "(– 4, –2)"]

A:

### Initial Solution Approach:

1. **Understanding Reflection**: Reflecting a point across y = x involves swapping its x and y coordinates.
2. **Applying Reflection**:
   - Vertex (–2, –4) reflects to (–4, –2).
   - Vertex (–4, 1) to (1, –4).
   - Vertex (–1, 4) to (4, –1).
   - Vertex (2, 4) to (4, 2).
   - Vertex (3, 0) to (0, 3).

**Conclusion**: Based on the initial understanding, one of the vertices of P' was identified as (4, –1).

### Let's verify this answer for consistency:

Upon reviewing the reflection process, the error becomes evident. The correct application of the reflection principle across the line y = x should indeed swap the coordinates, but my initial conclusion mistakenly listed a vertex not correctly reflected based on the provided vertices. The correct reflection of the given vertices should directly swap each vertex's x and y values without altering the sign or position of the numbers beyond their coordinate swap.

### Correct Reasoning and Answer:

Reflecting each vertex correctly:
- Vertex (–2, –4) indeed reflects to (–4, –2), matching the reflection rule.

Therefore, the **correct vertex of pentagon P'** after reflection is indeed **(–4, –2)**, aligning with the reflection principle and correcting the earlier mistake in identifying the outcome of the geometric transformation.

Answer: D

'''
FORMAT_REQUIREMENT='''
### Format Requirement

Remember that after verifying your answer for self-consistency, **provide the answer in the format: "Answer: [option A/B/C/D]".** Only include your selected option after 'Answer:' without extra information.

How about this question?
'''
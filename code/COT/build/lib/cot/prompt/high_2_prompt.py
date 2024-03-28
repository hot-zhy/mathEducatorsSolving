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

Carlos Montado was born on Saturday, November 9, 2002. On what day of the week will Carlos be 706 days old? (Spell out the entire day of the week.
"options": ["Friday", "Thursday", "Wednesday", "Tuesday"]

A:

To find the weekday Carlos Montado will be 706 days old from his birthdate on Saturday, November 9, 2002, we can simplify the calculation as follows:

1. **Calculate Days Offset**: Since there are 7 days in a week, determine the offset by calculating `706 mod 7`.
2. **Determine Weekday**: Starting from Saturday, count forward by the offset to find the resulting weekday.

### Calculation
- Offset: `706 mod 7 = 6`
- Starting from Saturday and counting forward 6 days lands on **Friday**.

### Let's verify this answer for consistency:
To ensure the solution's consistency, we verify that counting 6 days forward from Saturday indeed results in Friday. This approach bypasses the need for detailed year and month calculations, focusing directly on the day-of-week progression.

**Conclusion**: Carlos will be 706 days old on a **Friday**. 

Answer: A
'''
FORMAT_REQUIREMENT='''
### Format Requirement

Remember that after verifying your answer for self-consistency, **provide the answer in the format: "Answer: [option A/B/C/D]".** Only include your selected option after 'Answer:' without extra information.

How about this question?
'''
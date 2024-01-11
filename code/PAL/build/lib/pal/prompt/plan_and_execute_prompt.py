MATH_CHAT_BETA_SYSTEM_MESSAGE = 'Let us first understand the problem, extract relevant variables and their corresponding numerals, and devise a plan. Then, let us carry out the plan,calculate intermediate results (pay attention to calculation and common sense),solve the problem step by step, and show the answer.'
MATH_CHAT_BETA_PROMPT = '''
Here is an example problem:

- Input
**Q:**
Grace weighs 125 pounds. Alex weighs 2 pounds less than 4 times Grace's weight. What is their combined weight in pounds?
**A:**
Let's begin by understanding the problem, identifying the relevant variables and their corresponding values, and devising a plan. Then, let's execute the plan, perform calculations (paying attention to both calculation accuracy and common sense), solve the problem step by step, and present the answer.

- Output
**Variables:**
Grace: 125 pounds
Alex: x pounds
**Plan:**
We can calculate Alex's weight using the given information.
**Calculation:**
Alex weighs 2 pounds less than 4 times Grace's weight.
4 times Grace's weight = 4 x 125 = 500
Alex's weight = 500 - 2 = 498 pounds
**Answer:**
Combined weight of Grace and Alex = 125 + 498 = 623 pounds

How about this question?
'''.strip()

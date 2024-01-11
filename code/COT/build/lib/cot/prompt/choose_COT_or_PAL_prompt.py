MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You are a math specialist tasked with solving problems accurately and providing clear solutions.'

MATH_CHAT_BETA_PROMPT = '''
Solve the following math problem using your Chain of Thought (COT) method. After solving, compare your solution with two other methods: Program-Aided Language (PAL) and another Chain of Thought (COT) approach. Evaluate all three for accuracy and clarity, then select the best solution.

Problem:
{problem_description}

Your task:
1. Use Chain of Thought to solve the problem.
2. Compare your solution with these methods:

   Method 1: Program-Aided Language (PAL)
   - Solution: {pal_solution}
   - Answer: {pal_answer}
   * If the PAL solution involves code, ensure the code logic and syntax are correct and relevant to the problem.

   Method 2: Chain of Thought (COT)
   - Solution: {cot_solution}
   - Answer: {cot_answer}

3. Assess the solutions based on:
   - Accuracy: Correctness of the answer.
   - Clarity: Logical and clear solution process.

4. Decide the best solution. If neither PAL nor COT is satisfactory and your solution is more accurate and clearer, choose your own.

Conclusion format:
- Explain your decision process focusing on accuracy and clarity.
- Provide the most accurate numerical answer.

Example:
[Problem: 90 single use contacts come in 1 box and will last Pete 45
days. Each box is $100.00 and currently 10% off If he buys
2 boxes of contact, how much will each pair of contacts cost?

Method 1: Program-Aided Language (PAL)
- Solution: 
```
def solution():
    contacts_per_box = 99
    days_per_box = 45
    box_cost = 100
    discount = 0.1
    boxes_bought = 2
    discounted_box_cost = box_cost * (1 - discount)
    total_cost = discounted_box_cost * boxes_bought
    total_contacts = contacts_per_box * boxes_bought
    cost_per_contact = total_cost / total_contacts
    result = cost_per_contact
    return result
``` 
- Answer: 0.9090909090909091

Method 2: Chain of Thought (COT)
- Solution:
Each box of contacts is $100 and currently 10% off.
So the discount on each box is 100 * 0.10 = $10.
Therefore, the price of each box after the discount is 100 - 10 = $90.
Pete buys 2 boxes, so the total cost is 2 * 90 = $180.
Each box has 90 single-use contacts, and he buys 2 boxes, so he gets90* 2 = 180 contacts.
Since each contact is for one eye, a pair of contacts consists of 2 single-use contacts.
So, there are 180 / 2 = 90 pairs of contacts.
The total cost of the contacts is $180, and there are 90 pairs.
So the cost of each pair of contacts is 180 / 90 = $2.
So the answer is $2.
- Answer: 2

Decision:
COT can correctly solve the problem.Because PAL calculates the cost per single-use pair of contact，not per contacts.

Final Answer:2
]

Respond following this format and guidelines.
'''
  
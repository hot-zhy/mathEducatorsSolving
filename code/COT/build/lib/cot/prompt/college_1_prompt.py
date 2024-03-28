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

Up to isomorphism, how many additive abelian groups G of order 16 have the property that x + x + x + x = 0 for each x in G ?
"options": ["0", "1", "2", "3"]

A:

To solve this problem, let's apply the chain of thought and self-consistency verification approach as requested.

### Step 1: Understand the Problem

We're tasked with finding the number of additive abelian groups \(G\) of order 16 that satisfy the property \(x + x + x + x = 0\) for each \(x\) in \(G\). The possible answers are:

- A: 0
- B: 1
- C: 2
- D: 3

### Step 2: Solve the Problem

An additive abelian group \(G\) of order 16 that satisfies \(x + x + x + x = 0\) for each \(x\) in \(G\) is a group where every element is of order 1, 2, or 4. This is because the equation implies that 4 times any element results in the identity element (0 in this context).

Given the order of the group is 16, we know from the fundamental theorem of finitely generated abelian groups that \(G\) can be expressed as a direct sum of cyclic groups of prime power order. Since the group must satisfy \(4x = 0\), this limits our components to be \(\mathbb{Z}_2\), \(\mathbb{Z}_4\), and \(\mathbb{Z}_2 \times \mathbb{Z}_2\) (because \(\mathbb{Z}_4\) and \(\mathbb{Z}_2 \times \mathbb{Z}_2\) are the only groups of order 4 where the property holds for all elements).

Considering the groups of order 16 that can be built under these constraints, we have:

1. \(\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2\) (all elements have order 2, satisfying the condition)
2. \(\mathbb{Z}_4 \times \mathbb{Z}_2 \times \mathbb{Z}_2\) (contains elements of order 4 and 2, satisfying the condition)
3. \(\mathbb{Z}_4 \times \mathbb{Z}_4\) (all elements have orders 1, 2, or 4, satisfying the condition)

These groups are all distinct up to isomorphism and satisfy the given property.

### Initial Answer

The correct answer is **D: 3**.

### Verification: Let's verify this answer for consistency

Considering the group property \(x + x + x + x = 0\), we conclude that all elements of the group must have orders that divide 4. The groups identified (\(\mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2 \times \mathbb{Z}_2\), \(\mathbb{Z}_4 \times \mathbb{Z}_2 \times \mathbb{Z}_2\), and \(\mathbb{Z}_4 \times \mathbb{Z}_4\)) all satisfy this criterion and are distinct in structure, thus are non-isomorphic to each other. Each of these groups is of order 16 and adheres to the condition provided. No other configuration of cyclic groups of order 16 would satisfy the specific requirement without redundancy or violating the order constraint.

Hence, upon verification, the initial answer **D: 3** remains consistent with the mathematical reasoning and the constraints of the problem.

Answer: D

'''
FORMAT_REQUIREMENT='''
### Format Requirement

Remember that after verifying your answer for self-consistency, **provide the answer in the format: "Answer: [option A/B/C/D]".** Only include your selected option after 'Answer:' without extra information.

How about this question?
'''
MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use the relevant knowledge of Applied mathematics and basic arithmetic for reasoning. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''   

Let's use the relevant knowledge of Applied mathematics and basic arithmetic to solve math problems. Here are five examples how to do it.
!!important
**
you must use python and response in the following structure
Please structure your code response in the same format as the following examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

```
def solution():
    # your code
    return result
```
**

Question:
Amy has $$37$$ apples and John has $$15$$ apples. How many apples does Amy have to give John so that she has exactly $$4$$ more apples than John?
```
def solution():
    # Amy has 37 apples and John has 15 apples.
    # Amy needs to give x apples to John so that she has 4 more apples than John.

    # Let x be the number of apples Amy gives to John.
    # After giving x apples, Amy will have 37 - x apples and John will have 15 + x apples.
    # The condition is 37 - x = 15 + x + 4.

    from sympy import symbols, Eq, solve

    x = symbols('x')
    # Set up the equation
    equation = Eq(37 - x, 15 + x + 4)

    # Solve for x
    number_of_apples_to_give = solve(equation, x)[0]
    result = number_of_apples_to_give
    return result
```


Question:
Mary is in a small class of $$6$$ pupils, but was absent for the Maths test last week. The other five pupils scored an average of $$72 \\%$$. Mary wrote the test this week and, with her score included, the class average went up to $$75 \\%$$.  What mark did Mary score on the test?  Answer~\\uline{~~~~~~~~~~}~ 
```
def solution():
    # The problem is to find the mark Mary scored on the test.
    # There are 6 pupils in total. The average score of the other 5 pupils was 72%.
    # With Mary's score included, the average for all 6 pupils is 75%.

    # Let M be the mark Mary scored.
    # The total marks of the other 5 pupils is 5 * 72.
    # The total marks for all 6 pupils including Mary is 6 * 75.
    # So, M + 5 * 72 = 6 * 75.

    # Solve for M.

    # Total marks of other 5 pupils
    total_marks_other_pupils = 5 * 72
    # Total marks for all 6 pupils
    total_marks_all_pupils = 6 * 75

    # Calculate Mary's mark
    marys_mark = total_marks_all_pupils - total_marks_other_pupils
    result = marys_mark
    return result
```


Question:
Find the average of the following sequence.  $$1$$, $$3$$, $$5$$, $$7$$, $$9$$, $$\\cdots $$, $$195$$, $$197$$, $$199$$.
```
def solution():
    # The task is to find the average of an arithmetic sequence: 1, 3, 5, ..., 197, 199.
    # This sequence is an arithmetic progression with a common difference of 2.
    # The first term a = 1 and the last term l = 199.
    # The formula for the average of an arithmetic sequence is (first term + last term) / 2.

    first_term = 1
    last_term = 199

    # Calculate the average
    average = (first_term + last_term) / 2
    result = average
    return result 
```


Question:
One of the angles in a triangle is a right angle. Two unknown angles are left and one of them is two times larger than the the other angle.  What is the size of the largest angle betwen the two?
```
def solution():
    # Given data: one angle is a right angle (90 degrees)
    # Let x be the smaller of the two unknown angles
    # The other angle is 2x

    # Sum of angles in a triangle is 180 degrees
    # 90 (right angle) + x + 2x = 180
    # 3x = 180 - 90
    # x = (180 - 90) / 3

    x = (180 - 90) / 3
    largest_angle = 2 * x  # The largest of the two unknown angles

    result = largest_angle
    return result
```


Question:
There are $42$ sweets in Container A and $4$ times as many sweets in Container B as Container A. Given that there are twice as many sweets in Container C as Container B, how many sweets are there in Container C? 
```
def solution():
    # Number of sweets in Container A
    sweets_in_A = 42

    # Container B has 4 times as many sweets as Container A
    sweets_in_B = 4 * sweets_in_A

    # Container C has twice as many sweets as Container B
    sweets_in_C = 2 * sweets_in_B

    # The result is the number of sweets in Container C
    result = sweets_in_C
    return result
```

!!important
**
you must use python and response in the following structure
Please structure your code response in the same format as the following examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

```
def solution():
    # your code
    return result
```
**

How about this question? 
'''.strip()

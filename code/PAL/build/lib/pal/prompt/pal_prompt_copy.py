MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use combination,calculation of number and place values,ratio calculation and logical reasoning to solve math problems.Please think step by step. And respond briefly.'
MATH_CHAT_BETA_PROMPT = '''

Let's use combination,calculation of number and place values,ratio calculation and logical reasoning to help solve math problems. 
Here are some examples how to do it.
!!important
**The comments in the example code state what solution or knowledge point was used for this problem and ideas for solving the problem.**
Note that the examples are not always correct.
If you come across a similar type of question, try to use the example method to solve it.


Q: There are 9 different potted plants in a garden. How many ways can 4 potted plants be arranged in a row?

```
def solution():
    # The problem is to find the number of ways to arrange 4 out of 9 different potted plants in a row.
    # This is a permutation problem, which can be solved using the permutation formula P(n, k) = n! / (n - k)!
    # where n is the total number of items and k is the number of items to arrange.

    import math

    # Total number of potted plants
    n = 9

    # Number of potted plants to arrange
    k = 4

    # Calculate the number of ways using the permutation formula
    result = math.factorial(n) / math.factorial(n - k)

    return result
```


Q: Five students A, B, C, D, and E line up in a row. If A wants to stand in the middle of B and C (not necessarily next to each other) how many ways are there to arrange them?

```
def solution():
    import math
    # Calculating the number of ways based on the provided logic

    # A in position 2 or 4: 2 options for B and C's position and 3! ways for the other three spots
    a_pos_2_4 = 2 * math.factorial(3)

    # A in position 3: 2 options for B and C's position either side of A, and 2 possibilities for each of the 4 spots
    a_pos_3 = 2 * 2 * 2 * 2

    # Total number of ways
    result = a_pos_2_4 + a_pos_3 + a_pos_2_4

    return result
```


Q: The spring sports meeting is coming soon, and every student in Class 1 of Grade 6 has signed up for at least one event. If there are 40 students participating in skipping rope and 31 students participating in long jump, and 21 students participating in both events, how many students are participating in only one event?

```
def solution():
    # The problem is to find the number of students participating in **only** one event.
    # This can be solved using the principle of Inclusion-Exclusion.
    #we should adjust this formula to: Only one event=∣A∣+∣B∣−2×∣A∩B∣
    # Total students participating in only one event = 
    # Students in Skipping Rope + Students in Long Jump - 2 * Students in Both

    # Number of students participating in skipping rope
    skipping_rope = 40

    # Number of students participating in long jump
    long_jump = 31

    # Number of students participating in both
    both = 21

    # Calculate the number of students participating in only one event
    result = skipping_rope + long_jump - 2 * both

    return result

```

How about this question?

!!important
**
Please structure your code response in the same format as the previous examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the answer of the question**

```
def solution():
    # your code
    return result
```
**

How about this Question?

'''.strip()

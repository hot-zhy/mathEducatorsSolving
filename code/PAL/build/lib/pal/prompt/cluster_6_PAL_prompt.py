MATH_CHAT_BETA_SYSTEM_MESSAGE = 'Use computational techniques and mathematical formulas to solve math problems. Think step by step and respond briefly.'
MATH_CHAT_BETA_PROMPT = '''

Let's apply computational techniques and mathematical formulas for reasoning in solving math problems. Below are examples illustrating this approach. Note: These examples are for guidance, and their methods might need adaptation for different problems.

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

Here are some examples how to do it.
Q:Find the value of $$10\\times \\left(\\frac{2998+2999+3000}{2997+2998+2999+3000+3001}\\right)$$.
```
def solution():
    # Numerator sum: 2998 + 2999 + 3000
    numerator_sum = 2998 + 2999 + 3000

    # Denominator sum: 2997 + 2998 + 2999 + 3000 + 3001
    denominator_sum = 2997 + 2998 + 2999 + 3000 + 3001

    # Simplify the fraction
    fraction = numerator_sum / denominator_sum

    # Multiply the fraction by 10
    result = 10 * fraction

    return result
```
Q:$$\\left( {{2}^{2}}+{{4}^{2}}+\\cdots +{{18}^{2}}+{{20}^{2}} \\right)-\\left( {{1}^{2}}+{{3}^{2}}+\\cdots +{{17}^{2}}+{{19}^{2}} \\right)=$$~\\uline{~~~~~~~~~~}~． 
```
def solution():
    # The problem is to calculate the difference between the sum of squares of even numbers and the sum of squares of odd numbers in a given range.
    # The even numbers are 2, 4, ..., 18, 20 and the odd numbers are 1, 3, ..., 17, 19.
    # The formula for the sum of squares of the first n natural numbers is n(n + 1)(2n + 1)/6.

    # Function to calculate the sum of squares of first n natural numbers
    def sum_of_squares(n):
        return n * (n + 1) * (2 * n + 1) // 6

    # Sum of squares of even numbers from 2 to 20 (i.e., 2^2, 4^2, ..., 20^2)
    # This is equivalent to 4 times the sum of squares of the first 10 natural numbers
    sum_even_squares = 4 * sum_of_squares(10)

    # Sum of squares of odd numbers from 1 to 19 (i.e., 1^2, 3^2, ..., 19^2)
    # This is equivalent to the sum of squares of the first 19 natural numbers minus the sum of squares of the first 9 even numbers
    sum_odd_squares = sum_of_squares(19) - 4 * sum_of_squares(9)

    # Calculating the difference
    result = sum_even_squares - sum_odd_squares

    return result

```

Q:Calculate the following fraction: $$\\frac{1}{2015^{3}-2014 \\times (2015^{2} + 2016)}$$.
```
def solution():
    # The problem is to simplify and calculate the fraction 1 / (2015^3 - 2014 * (2015^2 + 2016)).
    # This can be solved by expanding and simplifying the expression in the denominator.

    # Expand 2015^3 and 2014 * (2015^2 + 2016)
    denominator = 2015**3 - 2014 * (2015**2 + 2016)

    # Simplify the expression
    # We can factorize the expression or simplify it using basic algebraic operations

    # Calculate the value of the fraction
    fraction_value = 1 / denominator
    
    result=fraction_value

    return result

```

Q:$\\left( {{2}^{2}}+{{4}^{2}}+\\cdots +{{18}^{2}}+{{20}^{2}} \\right)-\\left( {{1}^{2}}+{{3}^{2}}+\\cdots +{{17}^{2}}+{{19}^{2}} \\right)=$$~\\uline{~~~~~~~~~~}~
```
def solution():
	total_sum = sum([x ** 2 for x in range(2, 21, 2)])
	odd_sum = sum([x ** 2 for x in range(1, 20, 2)])
	result = total_sum - odd_sum

	return result
```
Q:Given that  $$\\left( 1+\\frac{1}{2} \\right)\\times \\left( 1+\\frac{1}{{{2}^{2}}} \\right)\\times \\left( 1+\\frac{1}{{{2}^{4}}} \\right)\\times \\left( 1+\\frac{1}{{{2}^{8}}} \\right)\\times \\cdots \\times \\left( 1+\\frac{1}{{{2}^{{{2}^{2009}}}}} \\right)$$$$=2\\left( 1-\\frac{1}{{{2}^{{{2}^{n}}}}} \\right)$$,  find the value of $$n$$.
```
def solution():
    # Analyze the left and right sides of the equation and directly compare the exponential forms to find the value of n.
    # Left side simplifies to 2^(2^2010) / 2
    # The right side is 2 * (1 - 1/(2^(2^n)))
    # By comparison, we can solve for the value of n.

    # Since 2^(2^2010) / 2 = 2^(2^2010 - 1), we can compare it to the right-hand side expression
    left_exponent = 2**2010 - 1
    right_exponent = 2**n # The exponent from the right-hand side expression

    # Since both sides of the equation are equal, left_exponent = right_exponent
    # So 2^n = 2^2010 - 1
    # This means n = 2010 - 1
    n = 2010 - 1
	result = n
    return result

```
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

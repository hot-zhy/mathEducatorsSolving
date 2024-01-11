MATH_CHAT_BETA_SYSTEM_MESSAGE = 'Welcome to the Math Chat! As a math problem specialist, I am here to help you. Please provide the necessary mathematical expressions for the following problem.'
MATH_CHAT_BETA_PROMPT = '''
## Step 1: Formulate Equations

In this step, you need to understand the problem, extract relevant variables and their corresponding numerals, and formulate several equations to solve the problem.

Please provide the necessary mathematical expressions below.

## Step 2: Solve Equations Using Python Code and Give the Final Answer

Now, using Python code, please solve the equations you formulated in the previous step and provide the final answer to this problem.

Here is an example problem:
**Problem:**
If Peter walks up an up-going escalator at the rate of 1 step per second, he is able to reach the top in 10 steps. If he increases his rate to 2 steps per second, he can reach the top in 16 steps. Find the number of steps of the escalator.

**Step 1: Formulate Equations:**

Denote the number of steps of the escalator as `S`.
Denote the speed of the escalator in steps per second as `E`.

When Peter walks at 1 step per second and takes 10 steps to reach the top, the escalator moves him an additional E steps per second for 10 seconds. 
So the total number of steps he covers is:10 + 10E = S
When Peter walks at 2 steps per second and takes 16 steps to reach the top, the escalator moves him an additional E steps per second for 8 seconds (since he takes half the time to cover twice the steps). 
So the total number of steps he covers is:16 + 8E = S
Now we have a system of two equations:
1) `10 + 10E = S`
2) `16 + 8E = S`

**Step 2: Solve Equations Using Python Code:**

To solve these equations, we will use the sympy library in Python.

```
def solution():
    from sympy import symbols, Eq, solve

    # Define variables
    E, S = symbols('E S')

    # Solve equations
    eq1 = Eq(10 + 10*E, S)
    eq2 = Eq(16 + 8*E, S)

    # Solve the system of equations
    solution = solve((eq1, eq2), (E, S))
    result = solution[S]

    # Return the final answer
    return result
```

!!important
**
Please structure your code response in the same format as the previous examples, which is as follows:

**you must 'return result' **in the end of** your code, which result is the final answer of the question**

```
def solution():
    # your code
    return result
```
Make sure to provide the necessary comments within the code to explain the steps and logic involved.
**

How about this question?
'''.strip()

MATH_CHAT_BETA_SYSTEM_MESSAGE = 'Utilize algebraic methods and iterative computations to solve math problems. Approach each problem step by step and respond succinctly.'
MATH_CHAT_BETA_PROMPT = '''

Let's apply algebraic methods and iterative computations for systematic problem-solving in mathematics. Below are examples demonstrating how to effectively use these techniques. Note: While these examples serve as guidance, their methods might require adaptation to suit different types of mathematical problems.

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
Q:\\textbf{Percentage Single Base}  65\\% of the animals in a farm were cows and the rest were goats. When 240 more cows and goats were added to the farm, the percentage of cows increased by 20\\% and the number of goats doubled. How many goats were there in the farm at first? 
```
def solution():
    # The problem is to find the initial number of goats in a farm.
    # Initially, 65% of the animals were cows and the rest were goats.
    # When 240 more animals were added, the percentage of cows increased to 85% and the number of goats doubled.
    
    # Let T be the total initial number of animals.
    # Initial number of cows C = 65% of T, and initial number of goats G = 35% of T.
    # After adding 240 animals, total becomes T + 240.
    # The number of goats doubles, so new number of goats = 2G.
    # New percentage of cows = 85% of (T + 240).

    # Solving for T and then finding G using these relations.

    from sympy import symbols, Eq, solve

    T = symbols('T')
    # Initial cows and goats
    C = 0.65 * T
    G = 0.35 * T

    # Equation after addition of animals
    new_total = T + 240
    new_cows = 0.85 * new_total  # 85% are now cows
    equation = Eq(new_cows, C + 240 - 2 * G)

    # Solve for T
    T_solution = solve(equation, T)[0]

    # Calculate initial number of goats
    G_initial = G.subs(T, T_solution)
    result = G_initial.evalf()
    return result

```
Q:Sally had some cupcakes. She had $72$ more chocolate cupcakes than vanilla cupcakes. She had $36$ lesser blueberry cupcakes than vanilla cupcakes. After selling $\\dfrac{1}{6}$~of the chocolate cupcakes, $\\dfrac{2}{3}$~of the vanilla cupcakes and $\\dfrac{7}{9}$~of the blueberry cupcakes, Sally is left with $427$ cupcakes altogether. How many chocolate cupcakes did Sally sell? 
```
def solution():
    # The problem is to find how many chocolate cupcakes Sally sold.
    # She had 72 more chocolate cupcakes than vanilla and 36 less blueberry cupcakes than vanilla.
    # After selling fractions of each type, she is left with 427 cupcakes altogether.

    # Let V be the number of vanilla cupcakes.
    # Then, chocolate cupcakes C = V + 72 and blueberry cupcakes B = V - 36.
    # Sally sold 1/6 of C, 2/3 of V, and 7/9 of B.
    # Total cupcakes after selling: 427 = C - 1/6C + V - 2/3V + B - 7/9B

    from sympy import symbols, Eq, solve

    V = symbols('V')
    C = V + 72  # Chocolate cupcakes
    B = V - 36  # Blueberry cupcakes

    # Equation after selling
    cupcakes_left = 427
    equation = Eq(cupcakes_left, C - C/6 + V - 2*V/3 + B - 7*B/9)

    # Solve for V
    V_solution = solve(equation, V)[0]

    # Calculate initial number of chocolate cupcakes
    C_initial = C.subs(V, V_solution)
    # Calculate how many chocolate cupcakes were sold
    chocolate_sold = C_initial / 6
    result = chocolate_sold.evalf()
    return result

```

Q:A year is called a Blackjack year if the sum of its digits is 21. For example, 1983 is a Blackjack year since 1+9+8+3=21. How many Blackjack years are there between 1900 and 2000? （⭐⭐⭐⭐）
```
def solution():
    # The task is to find the number of Blackjack years between 1900 and 2000.
    # A year is a Blackjack year if the sum of its digits equals 21.

    # The approach is to iterate through each year in the range and check if the sum of its digits is 21.
    
    def is_blackjack_year(year):
        # Function to check if a year is a Blackjack year
        return sum(int(digit) for digit in str(year)) == 21

    # Count Blackjack years between 1900 and 2000
    blackjack_years_count = 0
    for year in range(1900, 2001):  # Include 2000 in the range
        if is_blackjack_year(year):
            blackjack_years_count += 1

    result = blackjack_years_count
    return result

```

Q:Mrs Chen spent $$$36$$ on a number of plates and~$\\tfrac{3}{4}$~of the remaining money on a number of cups. If she had~$\\tfrac{1}{6}$~of the original sum of money left, how much money did she have at first? 
```
def solution():
    # The problem is to find out how much money Mrs. Chen had originally.
    # She spent $36 on plates and 3/4 of the remaining money on cups. She had 1/6 of the original money left.

    # Let's denote the original sum of money as X.
    # After spending $36 on plates, she had X - $36 left.
    # Then, she spent 3/4 of the remaining money on cups, leaving her with 1/4 of (X - $36).
    # Finally, she had 1/6 of the original sum, X, left.

    # We can set up an equation: 1/6 * X = 1/4 * (X - $36).

    from sympy import symbols, Eq, solve

    X = symbols('X')
    # Equation based on the problem's description
    equation = Eq(1/6 * X, 1/4 * (X - 36))

    # Solve for X
    original_sum = solve(equation, X)[0]
    result = original_sum.evalf()
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

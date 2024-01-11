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
Q:A youth club has $50$ male and $70$ female members. $16 \\%$ of the male members and $10 \\%$ of the female members are students. What percentage of the members are students?
```
def solution():
    # Total number of members in the club
    total_members = 50 + 70  # sum of male and female members

    # Calculating the number of students among male and female members
    student_males = 16 / 100 * 50  # 16% of male members
    student_females = 10 / 100 * 70  # 10% of female members

    # Total number of students
    total_students = student_males + student_females  # sum of male and female student members

    # Calculating the percentage of students in the club
    percentage_students = (total_students / total_members) * 100
    result = percentage_students
    return result

```
Q:In a dice game, two dice are thrown together and the results added. A player with a £$$1$$ bet receives £$$10$$ if the total of two dice is greater than $$10$$. If this game is played $$60$$ times, how much will this player expect to lose?
```
def solution():
    # The problem is to calculate the expected loss for a player in a dice game.
    # A player bets £1 and receives £10 if the total of two dice is greater than 10.
    # The game is played 60 times.

    # Probability of rolling a total greater than 10 with two dice
    # The combinations for a total greater than 10 are (5,6), (6,5), (6,6), totaling 3 possibilities.
    # There are 6x6 = 36 possible outcomes when rolling two dice.
    probability_win = 3 / 36

    # Expected value of a single game
    # The player either wins £10 (with probability of winning) or loses £1 (with probability of losing)
    expected_value_per_game = (probability_win * 10) - ((1 - probability_win) * 1)

    # Expected total loss over 60 games
    expected_total_loss = 60 * expected_value_per_game
    result = expected_total_loss
    return result

```

Q:Eddie attended a math competition which had a total of $$10$$ questions. Every correct answer is awarded $$10$$ points while incorrect answers will result in a loss of $$3$$ points. Eddie answered all the questions but only gained $$48$$ points. How many questions did he answer incorrectly?
```
def solution():
    # The problem is to find the number of questions Eddie answered incorrectly in a math competition.
    # Given: 
    # Total questions = 10
    # Points for a correct answer = +10
    # Points for an incorrect answer = -3
    # Total points gained = 48

    # Let x be the number of correct answers and y be the number of incorrect answers.
    # We have two equations: x + y = 10 (total questions) and 10x - 3y = 48 (total points).

    # Solving these equations simultaneously
    # From x + y = 10, we get x = 10 - y
    # Substituting x in the second equation: 10(10 - y) - 3y = 48

    # Simplifying the equation
    # 100 - 10y - 3y = 48
    # -13y = 48 - 100
    # -13y = -52

    # Solving for y
    y = -52 / -13

    return y

```

Q:The operation \"☀\" is defined as, $1$☀$6 = 1 + 3 + 5 +7 + 9 + 11 = 36$,  $2$☀$3 = 2 + 4 + 6 = 12$ , $3$☀$5 = 3 + 5 + 7 + 9 + 11 = 35$ .  According to the rules above, calculate: $1$☀$10$.
```
def solution():
    # The problem is to calculate the value of 1☀10 using the defined "☀" operation.
    # Based on the examples given, the "☀" operation sums a sequence of odd numbers.
    # The sequence starts from the first number of the operation (1 in this case)
    # and continues with the next consecutive odd numbers until the count of numbers equals the second number of the operation (10 in this case).

    # Initialize the sum
    sum_sequence = 0

    # Start with the first number and add the next consecutive odd numbers
    for i in range(10):  # 10 is the second number in the operation, determining the count
        sum_sequence += (2 * i + 1)  # Formula to generate the ith odd number starting from 1
    result = sum_sequence

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

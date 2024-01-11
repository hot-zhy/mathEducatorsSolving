MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use method of ratio calculation, addition, subtraction, grouping method to solve math problems.Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''

Let's use ratio calculation, addition, subtraction, grouping method to help solve math problems. 
Here are some examples how to do it.
!!important
**The comments in the example code state what solution or knowledge point was used for this problem and ideas for solving the problem.**
Note that the examples are not always correct.
If you come across a similar type of question, try to use the example method to solve it.

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

Q: Alyson, Clara and Joyce were each given a piece of string of equal length. Alyson cut hers into smaller $$2\\text{m}$$ pieces, Clara cut hers into smaller $$3\\text{m}$$ pieces, and Joyce cut hers into smaller $$5\\text{m}$$ pieces. If there were no remainder in each case, find the shortest possible length of string given to each of them.

```
def solution():
    # The problem is to find the shortest possible length of string given to Alyson, Clara, and Joyce,
    # such that it can be divided into 2m, 3m, and 5m pieces without any remainder.
    # This is essentially finding the least common multiple (LCM) of 2, 3, and 5.

    from math import gcd

    # Function to find LCM of two numbers
    def lcm(x, y):
        return x * y // gcd(x, y)

    # Finding LCM of 2, 3, and 5
    result = lcm(lcm(2, 3), 5)

    return result
```

Q: An arrow is shot from the roof of a building 30 meters high at 5 m/s and at an angle of 45 degrees. How fast will the arrow be going when it hits the ground? 
```
def solution():
	import math
	# Given values
	initial_speed = 5  # m/s
	angle_degrees = 45  # degrees
	height = 30  # meters
	g = 9.81  # m/s^2, acceleration due to gravity
	# Convert angle to radians for calculation
	angle_radians = math.radians(angle_degrees)
	# Initial horizontal and vertical velocities
	initial_velocity_x = initial_speed * math.cos(angle_radians)
	initial_velocity_y = initial_speed * math.sin(angle_radians)
	# Final vertical velocity using v^2 = u^2 + 2as
	final_velocity_y_squared = initial_velocity_y**2 + 2 * g * height
	final_velocity_y = math.sqrt(final_velocity_y_squared)
	# Final speed of the arrow when it hits the ground (Pythagorean theorem)
	final_speed = math.sqrt(initial_velocity_x**2 + final_velocity_y**2)
	result = final_speed
    return result
```


Q: Alan and Phillip start at the same time and walk from $A$ to $B$. It takes Phillip $12$ minutes to arrive at $B$. Phillip walks $15$ meters more than Alan does per minute. Given that Phillip arrives at $B$ $3$ minutes earlier than Alan does, find the distance between $A$ and $B$.

```
def solution():
    # The problem is to find the distance between points A and B.
    # Alan and Phillip start walking at the same time from A to B.
    # Phillip takes 12 minutes to arrive at B and walks 15 meters more per minute than Alan.
    # Phillip arrives 3 minutes earlier than Alan.

    # Let x be the speed of Alan in meters per minute.
    # Then, Phillip's speed is (x + 15) meters per minute.
    # Since Phillip takes 12 minutes, the distance AB = 12 * (x + 15).
    # Alan takes 12 + 3 = 15 minutes to cover the same distance, so AB = 15 * x.
    # Equating the two expressions for AB gives us 12 * (x + 15) = 15 * x.

    # Solving for x
    x = (12 * 15) / 3  # Simplified from 12x + 180 = 15x

    # Calculating the distance between A and B
    distance_AB = 12 * (x + 15)
	result = distance_AB
    return result
```

Q: On my clock\\textquotesingle s display, the time has just changed to $02:31$. How many minutes will it be until all the digits $0, 1, 2, 3$ next appear together again?
```
def solution():
    # The task is to find out how many minutes will pass until the digits 0, 1, 2, 3 next appear together on a clock's display.
    # Starting from 02:31, we need to check each subsequent minute until the digits 0, 1, 2, 3 all appear together in the time.
    # We consider the clock in 24-hour format to account for times past midnight.

    def contains_all_digits(time_str):
        # Check if the time contains all the digits 0, 1, 2, 3
        return all(digit in time_str for digit in "0123")

    # Start counting from 02:31
    hour = 2
    minute = 31
    minutes_passed = 0

    while True:
        minute += 1
        minutes_passed += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0

        # Format the time as a string
        time_str = f"{hour:02d}{minute:02d}"

        # Check if the time contains all required digits
        if contains_all_digits(time_str):
            break

    result = minutes_passed
    return result
```

Q: One morning, Sara goes out to exercise. At $$\\rm 6.30$$ a.m., Sara leaves home and jogs at a speed of $$8$$ km per hour. At $$\\rm 8.30 $$ a.m., she feels a little bit tired and walks at half her jogging speed. At $$\\rm 9.30$$ a.m., Sara ends her exercise. How many kilometres has Sara travelled during her exercise? 
```
def solution():
    # The problem involves calculating the distance covered by Sara during her exercise.
    # Distance = Speed x Time
    # Sara jogs from 6:30 am to 8:30 am (2 hours) at 8 km/h and walks from 8:30 am to 9:30 am (1 hour) at half her jogging speed.
    # Jogging speed in km/h
    jogging_speed = 8  # km/h
    # Walking speed is half of jogging speed
    walking_speed = jogging_speed / 2  # km/h
    # Time spent jogging (6:30 am to 8:30 am) in hours
    jogging_time = 2  # hours
    # Time spent walking (8:30 am to 9:30 am) in hours
    walking_time = 1  # hour
    # Calculate the total distance covered
    total_distance = (jogging_speed * jogging_time) + (walking_speed * walking_time)
	result = total_distance
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
How about this Question?

'''.strip()

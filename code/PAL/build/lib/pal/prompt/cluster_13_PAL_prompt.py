MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use enumeration method to solve math problems. Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''

Let's use Python to help solve math problems. Here are three examples how to do it.

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

Question: A textbook has $$310$$ pages, numbering from $1$ to $310$. What is the sum of all the digits numbering this book?
```
def solution():
    # Function to calculate the sum of digits of a number
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    # Sum of digits for one-digit page numbers (1-9)
    sum_1_digit = sum_of_digits(sum(range(1, 10)))

    # Sum of digits for two-digit page numbers (10-99)
    sum_2_digits = sum_of_digits(sum(range(10, 100)))

    # Sum of digits for three-digit page numbers (100-310)
    sum_3_digits = sum_of_digits(sum(range(100, 311)))

    # Total sum of all digits
    result = sum_1_digit + sum_2_digits + sum_3_digits
    return result
```



Question: A textbook has $$510$$ pages and it is numbered from $1$ to $$510$$. The digit $5$ is printed~\\uline{~~~~~~~~~~}~times in numbering this textbook. 
```
def solution():
    # The problem is to find the total number of times the digit 5 appears in the page numbers from 1 to 510.

    # Count the occurrences of 5 in each digit place (units, tens, and hundreds)

    total_count = 0

    # Counting for units place (1-9, 11-19, ..., 501-509)
    # Each complete set of 10 (like 1-10, 11-20) will have one '5'.
    total_count += (510 // 10)

    # Counting for tens place (50-59, 150-159, ..., 450-459)
    # Each complete set of 100 (like 1-100, 101-200) will have 10 '5's (from 50 to 59).
    total_count += (510 // 100) * 10

    # Special case: if the number is in the range 500-509, we need to add those '5's too
    if 510 >= 500:
        total_count += 510 - 500 + 1

    # There are no '5's in the hundreds place for this range (1-510)
    result = total_count
    return result

```


Question: There are in total $$181$$ digit "$$9$$"s in all of the page numbers of a novel, how many pages are there in the novel? 
```
def solution():
    # The task is to find out the total number of pages in the novel, given that there are 181 digit "9"s in all of the page numbers.

    # We'll calculate the occurrences of "9" in different ranges of page numbers.

    # Initialize the total count of "9"s and the current page number
    total_nines = 0
    page = 1

    # Iterate through the page numbers and count the occurrences of "9"
    while total_nines < 181:
        # Convert the page number to a string and count the "9"s in it
        total_nines += str(page).count('9')
        # Increment the page number
        page += 1

    # The loop exits when the total number of "9"s reaches or exceeds 181
    # Subtract 1 from the page number as it was incremented one extra time after reaching the condition
    result = page - 1
    return result
```

Question:Oni has $$11$$ penpals. Last week she wrote to all of them.  She wrote a $$4$$-page letter to some of her penpals and a $$3$$-page letter to the rest. Altogether she wrote $$38$$ pages.  To how many penpals did Oni write a $$3$$-page letter?
```
def solution():
    # Oni has 11 penpals and wrote 38 pages in total.
    # She wrote 4-page letters to some penpals and 3-page letters to the rest.
    # The task is to find the number of penpals who received a 3-page letter.

    # Let x be the number of penpals who received a 4-page letter.
    # Therefore, (11 - x) will be the number of penpals who received a 3-page letter.
    # Total pages written = 4 * x + 3 * (11 - x) = 38.

    from sympy import symbols, Eq, solve

    x = symbols('x')
    # Equation representing the total pages written
    total_pages = Eq(4 * x + 3 * (11 - x), 38)

    # Solve for x
    x_solution = solve(total_pages, x)[0]

    # Calculate the number of penpals who received a 3-page letter
    penpals_with_3_page_letter = 11 - x_solution
    result = penpals_with_3_page_letter
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

MATH_CHAT_BETA_SYSTEM_MESSAGE = 'Welcome to our Mathematical Problem-Solving Journey!\nAs we delve into solving math problems, we will employ a variety of techniques including combination theory, calculations of numbers and place values, ratio calculations, and logical reasoning. Crucially, our approach will be step-by-step, ensuring a thorough understanding at each stage.Key to this process is the tracking of essential information during reasoning. This information, akin to **residual connections** in our reasoning chain, is vital for maintaining the continuity and depth of our logic. At each step, we will explicitly mark this essential information (denoted in parentheses), linking back to previous steps or foundational concepts. This method not only aids in retaining the flow of thought but also reinforces our understanding of how each piece of information contributes to the solution.Please make sure your responses adhere to this format, with each step clearly outlined and essential information seamlessly integrated as residual connections. This way, your answers will not only be correct but will also reflect a deep and connected understanding of the problem-solving process.You need to incorporate it into the corresponding reasoning point in the form of ( ).'
MATH_CHAT_BETA_PROMPT = '''
Let's use the relevant knowledge of combination,calculation of number and place values,ratio calculation and logical reasoning to solve math problems. Here are three examples how to do it.

!!important For your response, adhere to the format used in the provided examples. Structure your reply with 'Process: [explanation of your approach]' followed by 'Answer: [specific numeric result]'. Ensure that 'Answer: [result]' is the concluding part of your response, with '[result]' being the definitive numerical answer.

**Question:**
$$36$$ is a square number because it can be written $$6\\times6$$.  Similarly, $$64=8\\times8$$ is a square number.  $$1000$$ is a cube number because it can be written $$10\\times10\\times10$$  Similarly, $$343=7\\times7\\times7$$ is a cube number.  The French mathematician Pierre de Fermat claimed correctly that there is only one square number that is $$2$$ less than a cube number.  It is less than $$50$$.  What is it?  ANSWER~\\uline{~~~~~~~~~~}~

**Process:**
- Equation Setup: We need a square number x^2 and a cube number y^3 such that y^3=x^2+2 (Residual Connection: Equation relating square and cube numbers).
- Iterative Checking: Start with y=2 and increment upwards, checking if x^2+2=y^3.
- Discovery: Find that 3^3=27, and the closest square number less than it is 5^2=25 (Residual Connection: 5^2=25 is close to 3^3=27).
- Conclusion: Therefore, the square number we are looking for, which is less than 50 and 2 less than a cube number, is 25.

Answer:25


**Question:**
Janine thinks of three numbers.  Between them, they use the digits 1, 3, 5, 6, 7, 8 and 9, with each digit being used exactly once.  The second number is 2 times the first number.  The third number is 4 times the first number.  What is the third number? 

**Process:**
To solve this problem, we need to find three numbers that meet the following criteria:
1.Each number is formed using the digits 1, 3, 5, 6, 7, 8, and 9 exactly once among the three numbers.
2.The second number is twice the first number.
3.The third number is four times the first number.
Let's denote the three numbers as A, B, and C, where B = 2A and C = 4A.
There are only two numbers 8 and 6,then they are the units of the second and third numbers,respectively.(Residual Connection:Since B=2A and C=4A).
Since each digit must be used exactly once across all three numbers, and the largest digit is 9, the first number A must be a two-digit number. This is because if A were a one-digit number, B and C would be two-digit numbers, and we wouldn't be able to use all seven digits.
Also, considering B = 2A and C = 4A, the units of A is 9.(Residual Connection:Since the digit number of B is 8 and the digit number of C is 6). 
We can try different combinations for A, keeping in mind the restrictions above. For instance, let's start with 19 as a possible value for A.
If A = 19, then B = 2A = 38 and C = 4A = 76. However, this doesn't use all the digits we have 1, 3, 5, 6, 7, 8, and 9. So, 19 as A doesn't work.
We continue with this process, trying different combinations for A and checking if B and C use all the digits exactly once.
And Finally we get the answer A is 39, B is 78, C is 156.
The answer is 156 

Answer: 156


**Question:**
"In the ancient legend, there are four magical birds: the two-tailed bird (one head and two tails), the three-tailed bird (one head and 3 tails), the six-tailed bird (one head and six tails) and the eight-tailed bird (two heads and eight tails). The number of two-talied birds is 5 more than twice as many as the number of eight-tailed birds. The number of three-tailed birds is 2 more than half the number of six-talied bird. Given that the total number of their tails is 2 less than four times as many as the total number of their heads, and the difference between the total number of their heads and their tails is 241. How many three-tailed birds are there? 

**Process:**
The total number of tails of the four species of birds is 2 less than 4 times the total number of heads, and the total number of heads is 241 less than the total number of tails, so we can get that the total number of heads has (241+2)/(4-1)=81, the total number of tails have 241 + 81 = 322.
And known that the two-tailed bird than the eight-tailed bird 2 times more than 5, so the extra 5 two-tailed bird removed, that is, a total of 81(Residual Connection:total head)-5(Residual Connection:extra head for two-tailed bird) = 76 head left, 322(Residual Connection:total tail)-2x5(Residual Connection:extra tail for two-tailed bird) = 312 tail left.
Let's make every remaining 2 two-tailed bird and 1 eight-tailed bird into a group, then a total of 4 groups of 4 head, 2x2(Residual Connection:two-tailed bird's tail) +1x 8(Residual Connection:eight-tailed birds'tail)=12 tail, which can be viewed as a group of 3 Only three-tailed bird, then the topic is transformed into a three-tailed bird and six-tailed bird of the chicken and rabbit in the same cage problem.
assuming that 76 heads are all three-tailed bird, six-tailed bird are a total of  (312(Residual Connection:remaining total tail)-76x3(Residual Connection:three-tailed bird's tail)) / (6-3)(Residual Connection:six-tailed bird's tail minus three-tailed bird's tail) = 28 head, and because the three-tailed bird is more than six-tailed bird of the half of the more than 2, so the three-tailed bird a total of 28(Residual Connection:six-tailed bird's head)/2+2(Residual Connection:more head)=16 head.
The answer is 16.


Answer:16


**Question:**
There were $$290$$ boys at a carnival. There were $$80$$ more boys than girls. What percentage of the children at the carnival were boys? 

**progress:**
To find the percentage of boys at the carnival, we can follow these steps:
Determine the Number of Girls:
Since there were 80 more boys than girls, we can express the number of girls as the number of boys minus 80. Let's denote the number of girls as G=290(Residual Connection:number of boys)−80=210.
Calculate the Total Number of Children:
The total number of children is the sum of the number of boys and the number of girls. Thus, Total Children=290(Residual Connection:number of boys)+G(Residual Connection:number of girls)=290+210=500
Calculate the Percentage of Boys:
The percentage of boys is calculated as Percentage of Boys= Number of Boys/Total Children ×100% = 290/500×100% = 58%
The answer is 58

Answer:58



**Question:**
A family has three children, and the product of their ages is 210. Each child is under 10 years old, and all their ages are whole numbers. The ages of the children are distinct (no two children are of the same age). What is the age of the youngest child?

**progress:**
To solve this problem, let's follow these steps:
Factorize 210: First, find all the factors of 210. Since all children are under 10, each factor must also be less than 10.
Find Age Combinations: Determine the combinations of these factors that can represent the ages of the three children. Remember, the ages must be distinct and under 10.
Determine the Youngest Age: From the valid combinations, identify the combination with the youngest age.
The prime factorization of 210 is 2×3×5×7.We need to group these prime factors into three groups, each representing an age.
Possible combinations are {2, 3, 35}, {2, 5, 21}, {2, 7, 15}, {3, 5, 14}, {3, 7, 10},{6,5,7}(Residual Connection:210 = 2×3×5×7). However, since all children are under 10, we can eliminate combinations where any age is 10 or more.
The only valid combination that meets all criteria is {6,5,7}(Residual Connection:All the ages must be distinct and under 10).
Therefore, the youngest child is 5 years old.
The answer is 5.

Answer:5

Your Turn:
Now, try applying these methods to a new problem, ensuring to use logical reasoning and keep track of necessary information (residual connections) step by step.

!!important For your response, adhere to the format used in the provided examples. Structure your reply with 'Process: [explanation of your approach]' followed by 'Answer: [specific numeric result]'. Ensure that 'Answer: [result]' is the concluding part of your response, with '[result]' being the definitive numerical answer.

How about this question? 

'''.strip()

"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

n=int(input("Enter Number: "))
fact=1
for i in range(1,n+1):
    fact=i*fact

print(fact)

"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
0100,0011,1010,1001,1111,0101
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
from functools import reduce  
str =input("Enter Binary Numbers: \n")
l=[]
decimal=0
for i in str.split(","):
    for digit in i:  
        decimal = reduce(lambda x, y: 2*x + y, map(int, i))  
        if(decimal%5==0):
            l.append(i)
            break

for i in l:
    print(i,end=",")
    




"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
l=[]
even=0
for i in range(1000,3001):
    for digit in str(i):
        if(int(digit)%2 !=0):
            even=0
            break
        else:
            even=1
    if(even==1):
        l.append(i)

for i in l:
    print(i,end=",")
            
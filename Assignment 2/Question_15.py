"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
x=int(input("Enter Digit: "))
ten=x*10+x
hundred=x*100+ten
thousand=x*1000+hundred
print(x+ten+hundred+thousand)

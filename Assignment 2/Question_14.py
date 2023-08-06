"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
str = input("Enter string: \n")
upper=lower=0
for i in str:
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1
    else:
        pass
print("UPPER CASE ", upper)
print("LOWER CASE ", lower)
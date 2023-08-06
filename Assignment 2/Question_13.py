"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
str = input("Enter string: \n")
digit=letters=0
for i in str:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letters=letters+1
    else:
        pass
print("Letters", letters)
print("Digits", digit)
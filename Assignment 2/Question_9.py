"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
print("Enter string: ")
str=list()
while True:
    uip = input()
    if uip == '':
        break
    else:
        str.append(uip)

for i in str:
    print (i.upper())
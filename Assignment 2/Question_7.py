"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


"""

x,y = input("Enter two values: ").split(",")
x=int(x)
y=int(y)
l1 = []
for i in range(x):
    l1.append([])
    for j in range(y):
        l1[i].append(i*j)
print(l1)
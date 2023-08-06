"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""

class Convet_upper:
    def __init__(self)->None:
        self.str = ""
        

    def getString(self):
        self.str=input("Enter String: ")
 
      
    def printString(self):
        print(self.str.upper())


def main():
    x=Convet_upper()
    x.getString()
    x.printString()

if __name__ == "__main__":
    main()
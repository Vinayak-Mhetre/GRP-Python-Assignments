"""   
    Name: Vinayak Mhetre
    TIAA: Week-2, Day-5, Python Session
    Question: Check the given word is palindrome or not.
"""
print("<=== Check the given word is palindrome or not ===>")
str=input("Enter Word: ")
if(str==str[::-1]):  
      print(str,"is a palindrome")  
else:  
      print(str ,"is not a palindrome") 

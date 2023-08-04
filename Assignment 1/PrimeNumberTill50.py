"""   
    Name: Vinayak Mhetre
    TIAA: Week-2, Day-5, Python Session
    Question: Print Prime number from list till 50.
"""
print("<=== Print Prime number from list till 50 ===>")
prime=[]
for i in range(2,51):
    for j in range(2,i):
        if(i%j == 0):  
            break;
    else:
        prime.append(i)    
            
print(prime)
    
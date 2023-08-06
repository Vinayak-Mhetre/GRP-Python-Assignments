"""
Name: Vinayak Mhetre
TIAA: Week-2, Day-5, Python Session.

Question 1
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

"""
begin=2000
end=3200
ans=[]
for i in range(begin,end+1):
    if((i%7==0) & (i%5!=0)):
        ans.append(i)

print(ans)
       
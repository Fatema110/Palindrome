"""
CHECK IF A NUMBER IS PALINDROME
"""

n=int(input(" enter the number "))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print(" The number is a Palindrome ")
else:
    print("The number is not a Palindrome ")
    
OUTPUT-
enter the number 123
The number is not a Palindrome 

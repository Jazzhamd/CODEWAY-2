import random
import string
n=int(input("\nEnter the desired length of your password:"))
complexity=input("\nEnter complexity level(low or high(includes punctuation characters)):")
if(complexity=="high"):
    allChar=string.ascii_letters + string.digits + string.punctuation
else:
    allChar=string.ascii_letters + string.digits
pswd=""
for i in range(n):
    pswd+=random.choice(allChar)
print("\nYour password is",pswd)




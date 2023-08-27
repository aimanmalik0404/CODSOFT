import random
import string
print("            Password Generator         ")
Username=input("Enter Username:")
length=int(input("Enter the length of password:"))
#x=int(input("Enter your choice:"))
charList=""
x=string.ascii_letters+string.digits+string.punctuation
charList+=x
password = []

for i in range(length):
	randomchar = random.choice(charList)
	password.append(randomchar)
print("The generated password is: " + "".join(password))
#print("The generated password is:", List)

        

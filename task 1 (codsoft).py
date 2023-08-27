print("            Calculator    ")
x=int(input("enter 1st number:"))
y=int(input("enter 2nd number:"))
z=input("Select operation:: +,-,*,/,//,%,** :")
if (z=="+"):
    print("The sum is:", x+y)
elif (z=="-"):
    print("The difference is:", x-y)
elif (z=="*"):
    print("The multiplication is:", x*y)
elif (z=="/"):
    print("The division is:", x/y)
elif (z=="//"):
    print("The floor division is:", x//y)
elif (z=="%"):
    print("The modulo is:", x%y)
else:
    print("The exponential is:", x**y)
#print("the sum of two numbers is:",x+y)
#print("the difference of two numbers is:",x-y)
#print("multiplication of two numbers is:",x*y)
#print("division of two numbers is:",x/y)
#print("floor division of two numbers is:",x//y)
#print("modulo of two numbers is:",x%y)
#print("exponential of two numbers is:",x**y)

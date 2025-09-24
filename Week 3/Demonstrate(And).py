# Demonstrate logical operators (and, or, not) with two conditions.
x = int(input("Enter first side: "))
y = int(input("Enter second side: "))
z = int(input("Enter Third side: "))
if (x==y and y==z and z==x):
    print("Its an equilateral triangle!")
elif (x==y and y==z and z!=x):
    print("Its an isosels triangle!")
elif (x!=y and y!=z and z!=x):
    print("Its a scalene triangle!") 
else:
    print("Invalid input")

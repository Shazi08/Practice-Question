# Write a program to calculate sum, difference, product, and division of two numbers.
x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
option = int(input("Enter your option number {1.Add 2.Subtract 3.Multiplication 4.DIvision}: "))
if option==1:
    print("Addition: ",x+y)
elif option==2:
    print("Subtraction: ",x-y)
elif option==3:
    print("Multiplication: ",x*y)
elif option==4:
    print("Division: ",x/y)
else:
    print("Invalid option!!!3")
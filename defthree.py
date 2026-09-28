def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print(f"Sum: {add(num1,num2)}")
print(f"Difference: {subtract(num1,num2)}")
print(f"Product: {multiply(num1,num2)}")
print(f"Quotient: {divide(num1,num2)}")

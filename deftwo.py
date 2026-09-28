def rf(n):
    if n==1:
        return n
    else:
        return n*rf(n-1)
num=int(input("Enter a number: "))
if num<0:
    print("Sorry, Factorial Does Not Exist, ERROR FDNE404")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is {rf(num)}")
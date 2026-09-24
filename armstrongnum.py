def isarm(n):
    ns=str(n)
    power=len(ns)
    total=sum(int(digit)**power for digit in ns)
    return total==n
n=int(input("Enter a number: "))
if isarm(n):
    print("Armstrong number.")
else:
    print("Not armstrong number.")
def formula(n):
    total=n*(n+1)//2
    return 1
def sumloop(n):
    total=0
    steps=0
    for student in range(1,n+1):
        total=total+student
        steps=steps+1
    return steps
def doubleloopsteps(n):
    total,steps=0,0
    for student in range(1,n+1):
        for point in range(1,student+1):
            total=total+1
            steps=steps+1
    return steps
print("      n   Formula      Loop   Double loop")
for n in [4,10,100,1000,2000]:
    formulacount=formula(n)
    sumloopcount=sumloop(n)
    sumdoubleloopcount=doubleloopsteps(n)
    print(f"{n:>6} {formulacount:>9} {sumloopcount:>9} {sumdoubleloopcount:>13}")
print()
print("n doubles from 1000 to 2000. How many times more steps?")
print("  Formula     x",formula(2000)/formula(1000))
print("  Loop     x",sumloop(2000)/sumloop(1000))
print("  Double Loop     x",doubleloopsteps(2000)/doubleloopsteps(1000))
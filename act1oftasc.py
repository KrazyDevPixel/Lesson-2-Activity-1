def sumformula(n):
    total=n*(n+1)//2
    steps=1
    return total, steps
def sumloop(n):
    total=0
    steps=0
    for student in range(1,n+1):
        total=total+student
        steps=steps+1
    return total, steps
def sumdoubleloop(n):
    total=0
    steps=0
    for student in range(1,n+1):
        for points in range(1,student+1):
            total=total+1
            steps=steps+1
    return total, steps
n=int(input("How many students are in the contest?: "))
print("Contest with n=",n,"students(student k earns k points)")
print()
total,steps=sumformula(n)
print("formula total: ",total,"steps:",steps)
total,steps=sumloop(n)
print("sumloop total: ",total,"steps:",steps)
total,steps=sumdoubleloop(n)
print("sumdoubleloop total: ",total,"steps:",steps)
print()
print("Same number, different number of steps.")
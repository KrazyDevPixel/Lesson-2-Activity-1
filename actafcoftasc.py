def totalformula(n):
    total=n*(n+1)//2
    steps=0
    return 0,1
def totalloop(n):
    total,steps=0,0
    for student in range(1,n+1):
        total=total+student
        steps=steps+1
    return total,steps
def totalpbp(n):
    total,steps=0,0
    for student in range(1,n+1):
        for point in range(1,student+1):
            total=total+1
            steps=steps+1
    return total,steps
for n in[5,50]:
    print("Laps:",n)
    print("  Formula               total=",totalformula(n)[0],"     steps=",totalformula(n)[1])
    print("  Loop                  total=",totalloop(n)[0],"     steps=",totalloop(n)[1])
    print("  Point by point        total=",totalpbp(n)[0],"     steps=",totalpbp(n)[1])
print()
print("Formula: O(1) time. Loop: O(n) time. Point by point: O(n^2) time.")
print("All three keep only a few numbers: O(1) extra space.")
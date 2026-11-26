print("FIRST PROJECT:")
def fml(scores):
    if len(scores)==0:
        return None,0
    picks=[scores[0],scores[len(scores)//2],scores[-1]]
    steps=3
    return picks,steps
def sba(scores):
    if len(scores)==0:
        return None,0
    total=0
    biggest=scores[0]
    steps=2
    for score in scores:
        total=total+score
        if score>biggest:
            biggest=score
        steps=steps+2
    average=total/len(scores)
    steps=steps+1
    return average,steps
def cwe(scores):
    notbigger=0
    steps=0
    for i in range(len(scores)):
        for j in range(i+1):
            if scores[j] <= scores[i]:
                notbigger=notbigger+1
            steps=steps+1
    return notbigger,steps
print("     n |   O(1): steps  /1 |   O(n): steps     /n |  O(n^2): steps      /n^2")
for n in [10,100,1000,2000]:
    scores=list(range(1,n+1))
    o1steps=fml(scores)[1]
    onsteps=sba(scores)[1]
    on2steps=cwe(scores)[1]
    ratioo1=o1steps/1
    ratioon=onsteps/n
    ratioon2=on2steps/(n*n)
print(f"{n:>6} | {o1steps:>11} {ratioo1:>4.0f} | {onsteps:>11} {ratioon:>6.3f} | {on2steps:>13} {ratioon2:>8.4f}")
print()
print("Exact counts: 3,2n+3 and n(n+1)/2=n^2/2+n/2.")
print("Divided by the domninant term (1,n, n^2) they settle to 3,2 and 0.5:")
print("drop the constant and the smaller terms -> O(1),O(n),O(n^2).")
print("SECOND PROJECT: ACCIDENTALLY SUBMITTED SAME PROJECT 2 TIMES."):
def ls(items,target):
    checks=0
    for i in range(len(items)):
        checks=checks+1
        if items[i]==target:
            return i,checks
    return -1,checks
scores=[3,7,2,9,4,1,8,5,6]
n=len(scores)
print("List:",scores,"  n =",n)
allchecks=[]
for target in scores:
    index,checks=ls(scores,target)
    allchecks.append(checks)
    print(f"  search {target}: found at index {index} after {checks} check(s)")
missing=int(input("Pick a number that is not in the list: "))
index, missingchecks=ls(scores,missing)
print(f"  search {missing}: index {index} (not in the list) after {missingchecks} checks")
print()
print("Best case: ",min(allchecks+[missingchecks]), "checks (target last or missing) -> Theta(n)")
avg=sum(allchecks)/n
print("Average   :", avg, "checks  (every position equally likely)=(n+1)/2=",(n+1)/2)
print("For every input: at most n checks -> O(n); at least 1 check -> Omega(1)")

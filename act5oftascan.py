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
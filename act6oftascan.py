def tliar(n):
    steps=0
    for i in range(n):
        steps=steps+1
    for j in range(n):
        steps=steps+1
    return steps
def lil(n):
    steps=0
    for i in range(n):
        for j in range(n):
            steps=steps+1
    return steps
def fil(n):
    steps=0
    for i in range(n):
        for j in range(5):
            steps=steps+1
    return steps
def tl(n):
    steps=0
    for i in range(n):
        for j in range(i+1):
            steps=steps+1
    return steps
shapes=[("two loops in a row",tliar),("loop inside loop",lil),("inner loop runs 5 times",fil), ("inner loop runs i+1 times", tl)]
print("shape                            n=10   n=100    n=1000  100->1000  Big-O")
for name, shape in shapes:
    steps10,steps100,steps1000=shape(10),shape(100),shape(1000)
    ratio=steps1000/steps100 if steps100>0 else 0
    if ratio<30:
        label="O(n)"
    else:
        label="O(n^2)"
    print(f"{name:<27} {steps10:>5} {steps100:>7} {steps1000:>9}  x{ratio:>7.1f}  {label}")
print()
print("Loops in a row add (n+n=2n). Loops inside loops muliply (nxn),")
print("unless the inner loop runs a fixed number of times (5xn is still O(n)).")
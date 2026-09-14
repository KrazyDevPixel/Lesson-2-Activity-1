snack="Chips"
price=0.21
quantity=10
isavailable=True
print(f"Snacks: {snack}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Available? : {isavailable}")
print(type(snack))
print(type(price))
print(type(quantity))
print(type(isavailable))
total=price*quantity
print(f"Total: {total}")
print(f"Sales price: {total-0.025}")
print(f"Double stock {quantity*2}")
print(f"Price under $1? {price<1}")
print(f"More than 5 in stock? {quantity>5}")
print(f"Price exactly $0.21? {price==0.21}")
shopname="Quick"+" "+"Bites"
print("Shop name: "+shopname)
print("Letters in name: ",len(shopname))
print("First letter: ",shopname[0])
a=1.50
b=3.00
print(f"Before: {a} and {b}")
temp=a
a=b
b=temp
print(f"After: {a} and {b}")
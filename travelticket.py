dest="Dhaka"
ticketprice=50.15
quantity=10
av=True
print("Destination: ",dest)
print("Ticket Price: ",ticketprice)
print("Quantity: ",quantity)
print("Available? : ",av)
print(type(dest))
print(type(ticketprice))
print(type(quantity))
print(type(av))
ttl=ticketprice*quantity
print(f"Total: {ttl}")
a=900.50
b=900.30
print("BEFORE: ",a," and ",b)
t=a
a=b
b=t
print("AFTER: ",a," and ",b)
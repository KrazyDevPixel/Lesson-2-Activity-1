city=input("Enter your city: ")
temp=int(input("Enter the temperature in Celsius: "))
if temp>32:
    print("It's a hot day!")
if temp<25:
    print("Nice weather today!")
else:
    print("You should wear a jacket.")
if temp>35:
    print("It's a very hot day!")
elif temp>25:
    print("Best weather ever!")
elif temp>15:
    print("It's a bit chilly today!")
elif temp>5:
    print("Cold!!")
else:
    print("Watch out for snow! Stay warm mate!")
import datetime
import calendar
now=datetime.datetime.now()
print("City: ",city)
print("Current time: ",now)
print(calendar.calendar(now.year))
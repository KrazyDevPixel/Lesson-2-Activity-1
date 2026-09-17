name=input("Enter your name: ")
mood=input("What is your mood? Happy/Angry/Sad/Neutral: ")
energylevel=input("What is your energy level? (High/Medium/Low): ")
if mood=="happy" and energylevel=="high":
    print(f"You are in a great mood {name}! Keep it up!")
elif mood=="happy" and energylevel=="medium":
    print(f"You are in a good mood {name}! Keep it up!")
elif mood=="happy" and energylevel=="low":
    print(f"You are in a nice mood {name}! Keep it up!")
elif mood=="sad" and energylevel=="high":
    print(f"Cheer up! {name}!")
elif mood=="sad" and energylevel=="medium":
    print(f"Cheer up! {name}!")
elif mood=="sad" and energylevel=="low":
    print(f"Cheer up! {name}!")
elif mood=="angry" and energylevel=="high":
    print(f"Chill out! {name}!")
elif mood=="angry" and energylevel=="medium":
    print(f"Chill out! {name}!")
elif mood=="angry" and energylevel=="low":
    print(f"Chill out! {name}!")
elif mood=="neutral" and energylevel=="high":
    print(f"Nice! {name}!")
elif mood=="neutral" and energylevel=="medium":
    print(f"Nice! {name}!")
elif mood=="neutral" and energylevel=="low":
    print(f"Nice! {name}!")
else:
    print("ERROR 404 NOT FOUND! Please enter a valid mood and energy level.")
class Pet:
    def __init__(self,name,health):
        self.name=name
        self.__health=health
    def showinfo(self):
        print(f"Pet name: {self.name}.")
        print(f"Pet health: {self.__health}.")
    def careaction(self):
        print(f"{self.name} needs general care.")
    def sethealth(self,newhealth):
        if newhealth>=0 and newhealth<=100:
            self.__health=newhealth
            print(f"{self.name}'s health updated to {self.__health}.")
        else:
            print("Health must be between 0 and 100.")
class Dog(Pet):
    def careaction(self):
        print(f"{self.name} needs playtime and a walk.")
class Cat(Pet):
    def careaction(self):
        print(f"{self.name} needs grooming and a quiet rest.")
class Rabbit(Pet):
    def careaction(self):
        print(f"{self.name} needs fresh carrots and a clean cage.")
dog=Dog("Buddy",85)
cat=Cat("Misty",84)
rabbit=Rabbit("Snowy",83)
pets=[dog,cat,rabbit]
print("My pet care dashboard: ")
for pet in pets:
    pet.showinfo()
    pet.careaction()
    print()
print("Updating pet health...")
dog.sethealth(100)
cat.sethealth(100)
rabbit.sethealth(100)
print("Final summary: ")
for pet in pets:
    pet.showinfo()
    print()
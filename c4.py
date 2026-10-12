class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        print(f"{self.name} is singing the song {song}.")
    def dance(self):
        print(f"{self.name} is now dancing.")
blu=Parrot("Blue",5)
print(blu.sing("'Happy"))
print(blu.dance())
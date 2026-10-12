class Robot:
    def __init__(self,name):
        self.name=name
    def sing(self,song):
        print(f"{self.name} is singing {song}")
    def talking(self):
        print(f"{self.name} is talking")
robotic=Robot("Harison")
print(robotic.sing("'The Robot Song'"))
print(robotic.talking())
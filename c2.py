class Student:
    grade=4
    name="Arham"
    def intro(self):
        print("I am a student.")
    def details(self):
        print("Hi my name is",self.name)
        print("I read in grade",self.grade)
ob=Student()
ob.intro()
ob.details()
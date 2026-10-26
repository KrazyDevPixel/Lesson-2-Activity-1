from abc import ABC,abstractmethod
class Animal:
    def __init__(self,name,habitat):
        self.name=name
        self.habitat=habitat
    def display(self):
        print(f"Animal: {self.name} | Habitat: {self.habitat}")
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def __init__(self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed=breed
    def speak(self):
        print(f"{self.name} ({self.breed}) says woof!")
class Parrot(Animal):
    def __init__(self,name,habitat,phrase):
        super().__init__(name,habitat)
        self.phrase=phrase
    def speak(self):
        print(f"{self.name} says {self.phrase}. {self.phrase}!")
class Lion(Animal):
    def __init__(self,name,habitat,pride):
        super().__init__(name,habitat)
        self.pride=pride
    def speak(self):
        print(f"{self.name} (PRIDE:{self.pride}) says ROARRR!")
dog=Dog("Bob","House","Bulldog")
parrot=Parrot("Max","Jungle","Squack")
lion=Lion("Sigma","Savannah","PRIDE SIGMA")
print("=====ANIMAL SOUND SHOW=====")
for animal in [dog,parrot,lion]:
    animal.display()
    animal.speak()
    print()

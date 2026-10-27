from abc import ABC, abstractmethod
class Instrument(ABC):
    def __init__(self,name,category):
        self.name=name
        self.category=category
    def displayinfo(self):
        print(f"Instrument name: {self.name}")
        print(f"Instrument category: {self.category}")
    @abstractmethod
    def playsound(self):
        pass
class Guitar(Instrument):
    def __init__(self,name,category,string):
        super().__init__(name,category)
        self.strings=self.strings
    def playsound(self):
        print(f"{self.name} has {self.strings} and soudns liek: strum strum!")
class Drum(Instrument):
    def __init__(self,name,category,drumt):
        super().__init__(name,category)
        self.drumt=self.drumt
    def playsound(self):
        print(f"{self.name} is a {self.drumt} and sounds like: boom boom!")
g=("Acoustic Guitar","String instrument",6)
d=("Bass Drum","Percussion instrument","Large drum")
for instrument in range[g,d]:
    instrument.displayinfo()
    instrument.speak()
    print()
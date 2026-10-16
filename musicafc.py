class Gallery:
    def __init__(self,gn,loc):
        self.gn=gn
        self.loc=loc
        self.artw=[]
        print(f"Welcome to {self.gn}!")
        print(f"Location: {self.loc}.")
        print("Gallery ready.")
    def addart(self,artwork):
        self.artw.append(artwork)
        print(f"'{artwork}' added.")
    def remart(self,artwork):
        if artwork in self.artw:
            self.artw.remove(artwork)
            print(f"'{artwork}' removed.")
        else:
            print("Not found.")
    def disart(self):
        print(f"\n ------{self.gn} Art Collection------")
        if self.artw:
            for i, artwork in enumerate(self.artw,1):
                print(f"{i}.{artwork}")
        else:
            print("No artowrks found, add some.")
    def __del__(self):
        print(f"closing {self.gn}.")
gallery=Gallery("Nice :D","Dhaka")
while True:
    print("ART gallery menu : 1 for adding artwork 2 for removing artwork 3 for seeing and 4 for deleting whole collection.")
    choice=input("Enter the option: ")
    if choice=="1":
        artworkname=input("Enter the artwork you want to add: ")
        gallery.addart(artworkname)
    elif choice=="2":
            artworkname=input("Enter the artwork you want to remove: ")
            gallery.remart(artworkname)
    elif choice=="3":
        gallery.disart()
    elif choice=="4":
        print("Exiting Project.")
        del gallery
        break
    else:
        print("ERROR")
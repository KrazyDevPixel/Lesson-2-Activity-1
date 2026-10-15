class Playlist:
    def __init__(self,name,genre):
        self.name=name
        self.genre=genre
        self.songs=[]
        print(f"Playlist '{self.name}' ({self.genre}) is ready.")
    def add_song(self,song):
        self.songs.append(song)
        print(f"{song} added to {self.name}")
    def rem_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print("{song} removed.")
        else:
            print("SONG NOT FOUND")
    def display(self):
        print(f"\n---{self.name} ({self.genre})---")
        if self.songs:
            for i, song in enumerate(self.songs,1):
                print(f"{i}.{song}")
        else:
            print("No songs found, add some.")
    def __del__(self):
        print("Playlist {self.name} deleted.")
mp=Playlist("Nice","Fun")
while True:
    print("1 for adding a song, 2 for removing a song, 3 to view playlist, and 4 to delete all[risky]")
    inp=int(input("Enter your option: "))
    if inp==1:
        song=input("Enter the name of the song you want to add: ")
        mp.add_song(song)
    elif inp==2:
        song=input("Enter the name of the song you want to add: ")
        mp.rem_song(song)
    elif inp==3:
        mp.display()
    elif inp==4:
        del mp
        break
    else:
        print("Enter 1,2,3 or 4. INVALID CHOICE DETECTED ERROR 1")
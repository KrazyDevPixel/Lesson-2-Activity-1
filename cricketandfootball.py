class Cricket:
    def __init__(self,player,score):
        self.__player=player
        self.__score=score
    def info(self):
        print(f"Player: {self.__player}, score: {self.__score}.")
    def play(self):
        print(f"{self.__player} hits a six!")
    def get_score(self):
        return self.__score
    def set_score(self,new_score):
        if new_score>=0:
            self.__score=new_score
            print(f"Score updated to {self.__score}.")
        else:
            print("Score cannot be negative!")
class Football:
    def __init__(self,player,score):
        self.__player=player
        self.__score=score
    def info(self):
        print(f"player: {self.__player}, score: {self.__score}.")
    def play(self):
        print(f"{self.__player} scores a hattrick! (3 goals)")
    def get_score(self):
        return self.__score
    def set_score(self,new_score):
        if new_score>=0:
            self.__score=new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative!")
cricket=Cricket("Rohit",85)
football=Football("Arjun",5)
print("Scoreboard")
for sport in (cricket,football):
    sport.info()
    sport.play()
    print()
print("Direct change attempt")
cricket.__score=999
print(f"get_score() still shows {cricket.get_score()}")
print("Updating score")
cricket.set_score(300)
football.set_score(9)
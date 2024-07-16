class sport():
    def __init__(self,player,position,age,exp):
        self.player=player
        self.position=position
        self.age=age
        self.exp=exp

    def details(self):
        print("player name :",self.player)
        print("position :",self.position)
        print("age :", self.age)
        print("exoerience :",self.exp)

s=sport("virat kohli","Captain",35,15)
s.details()
print("\n\tplayer 2\t")
s1=sport("rohit sharma","vice captain",40,16)
s1.details()



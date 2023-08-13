'''class Addition:
    def __init__(self, n1, n2):
       self.n1 = n1
       self.n2 = n2

    def add(self):
        print(self.n1+self.n2)


a1 = Addition(20, 2)
a2 = Addition(10, 5)

a1.add()
a2.add()'''


class Avengers:

    def __init__(self,Name,Age,Gender,SuperPower,Weapon):
       self.Name = Name
       self.Age = Age
       self.Gender = Gender
       self.SuperPower = SuperPower
       self.Weapon = Weapon
       self.isleader = False

    def avenger_details(self):
        print("Superheroes:",self.Name,self.Age,self.Gender,self.SuperPower,self.Weapon)

    def make_leader(self):
        self.isleader = True
        return "leader"

    def remove_leader(self):
        if self.isleader == False:
            return "she is alreday not a leader"
        else:
            self.isleader = False
            return "removed from leader successfully"



captianAmerica = Avengers("captain_America","50","Male","Super_Strength","Shield")
ironMan = Avengers("IronMan","40","Male","Technology","Armor")
blackWidow = Avengers("BlackWidow","35","Female","Superhumans","Batons")
hulk = Avengers("Hulk","60","Male","NA","Unlimitedstrength")
thor = Avengers("Hulk","58","Male","SuperEnergy","Bjoinir")
hawkeye = Avengers("Hawkeye", "25","female","fighting skills","Arrows")

Avengers.avenger_details(blackWidow)
print(Avengers.remove_leader(blackWidow))
print(Avengers.make_leader(blackWidow))
print(Avengers.remove_leader(blackWidow))








#in day 78 we are learn about single inheritance.........
class Animal:
    def __init__(self , name , species):
        self.name=name
        self.species=species

    def make_sound(self):
        print("sound mad by the animal")   


class Dog(Animal):
    def __init__(self ,name , breed):

     Animal.__init__(self , name , species="dog")
     self.breed=breed 

    def make_sound(self):
       print("Bark !!!!") 


d=Dog("dog" , "jarman shapeheard")
d.make_sound()

d2=Animal("Dog" , "Boxer")
d2.make_sound()


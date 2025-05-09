#in day 80 we are learn about multilevel inheritance.....
class Animal:
    def __init__(self , name , species):
        self.name=name
        self.species=species

    def show_detalis(self):
        print(f"name : {self.name}")
        print(f"species : {self.species}") 



class Dog(Animal):
    def __init__(self , name , breed):
        Animal.__init__(self  , name , species="Dog")
        self.breed=breed

    def show_detalis(self):
        Animal.show_detalis(self)
        print(f"breed : {self.breed}") 


class GlodenRetriver(Dog):
    def __init__(self , name , color):
        Dog.__init__(self  , name , breed="GlodenRetriver")
        self.color=color

    def show_detalis(self):
        Dog.show_detalis(self)
        print(f"color : {self.color}")

o=GlodenRetriver("tommy" , "black")
o.show_detalis() 

print(GlodenRetriver.mro())

        



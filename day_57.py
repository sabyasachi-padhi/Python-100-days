#in day 57 we are learn about classs and objects......


#class insialization......
class person:
    name="harry"
    occupation="software devloper"
    networth=10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()#object creation.....
b=person()#object creation.....
b.name="tarinee"
b.occupation="Navy officer"
b.networth=134
a.info()
b.info()

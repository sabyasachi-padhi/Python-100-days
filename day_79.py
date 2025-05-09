#in day 79 we are learn about multiple inheritance in python.......

class Employee:
    def __init__(self , name):
        self.name=name

    def show(self):
        print(f"the name is {self.name}")


class Dancer:
    def __init__(self , dance):
        self.dance=dance

    def show(self):
        print(f"the dance is {self.dance}") 


class Employee_dancer(Dancer , Employee):
    def __init__(self , name , dance):
        self.name=name
        self.dance=dance


d=Employee_dancer("harry" , "Hip-Hop")
d.show()

print(Employee_dancer.mro())#mro() method is order of method finding........



        
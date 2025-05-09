#in day 70 we are learn about how to use class methods as alternative constructer in python.....
class Empoloyee:
    def  __init__(self , name , salary):
        self.name=name
        self.salary=salary


    @classmethod
    def from_str(cls , string):
        return cls(string.split("-")[0] , int(string.split("-")[1]))    



e1=Empoloyee("harry" , 12000)
print(e1.name)
print(e1.salary) 


string="jhon-12000"
e2=Empoloyee.from_str(string)
print(e2.name)
print(e2.salary)

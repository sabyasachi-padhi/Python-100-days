#in day 71 we are learn  about dir() , __dict__ and help() method....

#x=[1,2,3]
#print(dir(x))#the dir function return a list of attribute and method avilable for an object..


class person:
    def __init__(self , name , age):
        self.name=name
        self.age=age

p=person("jhon" , 30)
print(p.__dict__)#the dict method returns dictionary reperentation of an object's attributes 


print(help(person))#the help function is used to get help documaintation for an object..

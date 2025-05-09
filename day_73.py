#in day 73 we are learn about magic mrethod and dunder method in python...

class Employee:
    name="harry"
    def __len__(self):
        i=0
        for i in self.name:
            i=i+1
        return i



e=Employee()
# print(e.name)
# print(len(e))

#str method convert the an object to string reprentation......
#__repr__ method also do same as __str__method.......
#def __str__(self):
    #return f"the name of the employee is {self.name}"

#def __call__(self):
     #print("hallo i am call method")


        
        
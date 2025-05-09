#in day 69 we are learn about class method in python.......
class Employee:
    company="Apple"

    def show(self):
        print(f"the name is {self.name} and company name is {self.company}")
        
    @classmethod
    def change_company(cls , newname):#this is a class method and takes class as an argument..
        cls.company=newname


e1=Employee()
e1.name="harry"
e1.show()
e1.change_company("Tesla")#it's only change for instance not for the class
e1.show()
print(Employee.company)        

        
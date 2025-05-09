#in day 66 we are learn about instance variable and class varibale...
#class variable assoiated with class 
#insatnce variable associated with object instantiation....

class Employee:
    company_name="Apple" #class  variable.....
    def __init__(self , name):
        self.name=name #instance variable
        self.raise_amount=0.02 #instance variable


    def show_details(self):
        print(f"the name of the employee is {self.name} and the raise amount in {self.company_name} is {self.raise_amount}")

       

emp1=Employee("harry")
emp1.raise_amount=0.3 #we can change the instance variable......
emp1.company_name="Apple india"
emp1.show_details()           

emp2=Employee("Rohan")
emp2.show_details()           
          
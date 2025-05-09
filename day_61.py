#in day 61 we are learn about inheritance in python
class Employee:

    def __init__(self , name , id):
        self.name=name
        self.id=id

    def employee_detail(self):
        print(f"Employee name is {self.name} and id is {self.id}")


class programmer(Employee):# this is inheritance in python........
    def show_language(self):
        print("default language is python")          


obj=programmer("harry" ,456)

obj.employee_detail()
obj.show_language()
        
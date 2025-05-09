#in day 72 we are learn  about super keyword in python.......
#the super keyword is used to reffer to the parent class......

class Employee:
    def parent_method(self):
        print("this is the parent method")


class Child_class(Employee):
    def child_method(self):
        print("this is a child method")


        super().parent_method()

child__object=Child_class()
child__object.child_method()        
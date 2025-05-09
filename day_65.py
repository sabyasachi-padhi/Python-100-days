#in day 65 we are learn about static method in python....
#for static method we don't need to create an object
#we don't need to give self as an argument for static method...


class Math:
    def __init__(self , num):
        self.num=num

    def add_to_num(self , n):
        return self.num + n

    @staticmethod
    def add(a, b):
     return a+b     


a=Math(5)
print(a.num)
print(a.add_to_num(6)) 


print(Math.add(1,2))

    
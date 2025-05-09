#in day 60 we are learn about getters and setter in python

class Myclass:

    def __init__(self , value):
        self._value=value

    def show(self):
        print(f"value is {self._value}")    

    @property #it is a getter.......
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter#this is a setter
    def ten_value(self , new_value):
        self._value=new_value/10    


obj=Myclass(34)
obj.ten_value=67
print(obj.ten_value)#it's method but we can accses it as an property using property decoretor
obj.show()
        

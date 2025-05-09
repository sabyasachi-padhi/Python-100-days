#in day 62 we are learn about acsess modifir in python....
#in python there is no concept of public  , privet , protected keyword

#for using (__) keyword we can make property privet....

#for using (obj._class_name__property_name) we can acsess privet property.....

#(obj._class_name__property_name) this concept is called name mangling.......

class Employee:
    def __init__(self):
        self.__name="harry"


a=Employee()
print(a._Employee__name)        

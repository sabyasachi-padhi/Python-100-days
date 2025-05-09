#in day 58 we are learn  about constructer in python.....
#constructer is used to insializing the object......
class person:
     
    #  def __init__(self):#this is a defult constructer...
    #     print("i am a constructer")
    def __init__(self , name, occupation):#parameterized constructer.
        self.name=name
        self.occupation=occupation

    def info(self):
        print(f"{self.name} is a {self.occupation}")    
a=person("Tarinee" , "Marin commando")
a.info()

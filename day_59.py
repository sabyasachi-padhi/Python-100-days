#in day 59 we are learn about decoretor in python.....
#decoretor takes function as an argument and modifys the function and return......
def greet(fx):
  def mfx(): 
    print("good morning")
    fx()
    print("thanks for using this function")

  return mfx 


@greet
def hallo():
    print("hallo")        

hallo()    

#in day 20 we are learn about function in python.....
import math
#function using string passing as an argument........
def name( fname , mname, lname):
  print("hallo" , fname , mname, lname)

name("tarinee" , "prasad", "Mohapatra")  

#function to find gmean of two number.......
#geometric mean of two number formula is sqrt(a * b).....
def gmean(a , b):
    return math.sqrt(a*b)

print(gmean(4,5))


#function to find grater between two number.....
def greater(a , b):
    
    if(a > b):
        print("first number is graeter")

    else:
        print("second number is greater")    

greater(12, 3)

#using pass key_word......

def islesser(a,b):
    pass#pass keyword is used when we want to use this function after some time.


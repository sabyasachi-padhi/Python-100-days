#in day 37 we are learn about use of finally keyword in python...
# code in finally block is allways executed.......it does not matter that the error ouccred or not 
try:
   l=[1,2,3,4]
   i=int(input("enter the index   : "))
   print(l[i])
except:
    print("invalid input") 
finally:
    print("i am allways executed")    
       
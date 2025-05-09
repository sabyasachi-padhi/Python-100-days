#in day 36 we are learn about exception handling in python.....
#try except is used to catch the error..........
# try:
#    a=input("enter the number : ")
#    print(f"multiplication tabel of {a} is : ")

#    for i in range(1 , 11):
#        print(f"{int(a)} x {i} = {int(a)*i}")
# except :
#     print("invalid input")       

try:
   l=[1,2,3,4]
   i=int(input("enter the index   : "))
   print(l[i])
except ValueError:
    print("number is not an integer")   
except IndexError:
    print("invalid index")
#we can use multiple except block for multiple errors.....       
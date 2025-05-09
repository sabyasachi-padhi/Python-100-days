#in day 42 we are learn about.......Enumerate function...in python

marks=[12 , 56 , 32 , 98 , 12 , 45 ,1 ,4]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("harry , excellent")
#     index=index+1    


#the same thing we are doing easily with the help of Enumerate function

for index , mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("harry , excellent")


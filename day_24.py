#in day 24 we are learn about tuple data type.....
#just like string tuple is also immutable.....that means we can not be change the tuple....

#tup=(1,)#type is int.....if you want to inslaized the tupel with one element then you need to put a ',' ........
#print(type(tup))

tup=(1 , 2 , 5 , 6 , "harry" , "tarinee")
print(tup)

print(tup[0])
print(tup[-2])


if 2 in tup:
    print("element is present in this tuple")
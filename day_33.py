#in day  33 we are learn about dictionary in python....
# dictionary is a colloection of key_value pair 
dic={"name" : "harry" , "age" : 19 , "jobroll" : "software engineer"}
print(dic["name"])#this is through an error if the key are not present in the dictionary /////in this way we can accsess the value of given key
# print(dic["age"])#in this way we can accsess the value of given key
# print(dic["jobroll"])#in this way we can accsess the value of given key
# print(".......................................................")
# print(dic.get("name"))#it is give a none value if the key are not present in the dictionary this is the another way to acsess the value of given key.....
# print(dic.get("age"))#this is the another way to acsess the value of given key.....
# print(dic.get("jobroll"))#this is the another way to acsess the value of given key.....



# print(dic)#print entire dictionary key_value pair......
# print(dic.keys())#if you want to print only keys then you use this...
# print(dic.values())#print all values


#for using for loop you can print all value f keys .......
for key in dic.keys():
    print(f"the value coresponding to key {key} is {dic[key]}")#for using f string we are print all key value pair .....

print(dic.items())#print all keya-value pair .........
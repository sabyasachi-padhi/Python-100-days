#in day 28 we are going to learn about f-string.....
letter="hy my name is {} and i am from {}"
name="tarinee"
country="india"

#print(letter.format(name , country))#this the old way to doing string formating using format method....

#insted of using format method we can use f-string to format a string.

print(f"hy my name is {name} and i am from {country}")#this the more convineance way to doing string formating.......

# txt="For only {price: .2f} dollars"
# print(txt.format(price=49.09999))#for using simple format method..

price=49.09999
print(f"For only {price: .2f} dollars")#for using f-string....
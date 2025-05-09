#in day 86 we are learn about......walrus opretor... in python...
#walrus opretor allows you to assign a value to a varible..within an expression

foods=list()
while (food := input("what food do you like ? ") != "quit"):
    foods.append(food)
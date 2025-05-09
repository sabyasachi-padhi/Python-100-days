#in day 48 we are learn about local vs global variable...and the use of global keyword.....

# x=4#global variable
# print(x)

# def hello():
#     x=5#local varibale
#     print(f"the local x is {x}")
#     print("hallo harry")

# print(f"the global x is {x}")

# hello()
# print(f"the global x is {x}")

x=10#global varibale

def my_function():

    global x # now we can make x as global variable inside the function
    x=9
    y=5#local variable
    print(y)

my_function()
print(x)
#print(y)# this will cause an error because y is a local variable and is not accessible outside of the function    
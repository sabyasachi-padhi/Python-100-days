# in day 21 we are learn about function argument ...

# write a function to find avrage of two number..
# def avrage(a=5 , b=6):
#     print("average is :" ,  a+b/2)

# avrage()


# find average of two number in another way.....
def avg(*number):  # (*number) takes the argument as tuple
    sum = 0
    for i in number:
     sum = sum+i

    print("average of numbers is", sum/len(number))


avg(2, 4, 5, 6)

#in day 30 we are learn about very immportant concept recursion......
#Factorial prgram using recursion.....

#..............................................................

#factorial(3)=3-factorial(3-1=2)
#factorial(3)=3 * factorial(2)
#factorial(3)=3 * 2 * factorial(2-1=1)
#factorial(3)=3 * 2 * factorial(1)
#factorial(3)=3 * 2 * 1
#factorial(3)=6......

#...............................................................

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))

#write a ricursive fucntion to find fibonacci sequence....

def fibonacci(n):
    '''this function print elelmnt at given position in fibonacci sequence'''
    if(n==1 or n==2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))            
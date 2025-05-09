#in day 91 we are going to learn about generetor in python....
#generetor in python is a special type of  function thst allows you to crate ittrable squenc of value....

def my_gen():
    for i in range(5):
        yield i#the yield statement return a value from generator and susspends the execution of the function untill th next value is requested

gen=my_gen()
# print(next(gen))#next function is used to requests next value from generator.....
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)

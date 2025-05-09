#in day 53 we are learn about map() , filter(), reduce() 

#MAP()
# def cube(x):
#     return x*x*x

# print(cube(2))

# l=[1,2,4,6,4,3]
# newl=[]
# for item in l:
#     newl.append(cube(item))

# newl=list(map(cube , l))

# print(newl)


#FILTER()

# def filter_function(x):
#     return x>2

# l=[1,2,4,6,4,3]

# #newl=list(filter(filter_function ,l))

# #using lambda function.......
# newl=list(filter(lambda x: x>2 , l))
# print(newl)


#REDUCE
from functools import reduce

def sum(x ,y):
    return x+y

l=[1,2,4,6,4,3]
new_sum=(reduce(sum , l))
print(new_sum)



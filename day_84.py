#in day 84 we are going to learn about time module in python....
import time
# def using_while():
#     i=0
#     while i < 1000:
#         i=i+1
#         print(i)

# def using_for():
#     for i in range(1000):
#         print(i)



# init=time.time()
# using_for()
# t1=time.time() - init
# init=time.time()
# using_while()
# print(time.time() - init)
# print(t1)

# print(4)
# time.sleep(3)
# print("this is printing after 3 second")

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S" ,t)
print(formatted_time)
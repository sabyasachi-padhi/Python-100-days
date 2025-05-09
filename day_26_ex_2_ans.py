#in day 15 we are doing our second exersize........

#Excersize........

#print good morning sir......according to time..........

import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
#hour=int(input("enter the hour : "))
print(hour)

if(hour >= 0 and hour<12):
    print("Good morning sir !!!")
elif(hour >= 12 and hour<17):
    print("Good afternoon sir !!!")
if(hour >= 17 and hour < 24):
    print("Good night sir !!!")        
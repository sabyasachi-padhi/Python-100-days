#in day 55 we are going to do an excersize....
#SNAKE WATER GUN...GAME.......


#in day 63 we are going to slove a excersize.........
import random

def check(user , computer):
    if(user == computer ):
        return 0

    if(user == 0 and computer== 2):
        return -1

    elif(user == 1 and computer== 0):
        return -1

    elif(user == 2 and computer== 1):
        return -1


    return 1



computer=random.randint(0,2)
user=int(input("enter 0 for snake , 1 for water , 2 for gun : "))


score=check(user  , computer)

print("you : " ,  user)
print("computer : " , computer)

if(score == 0):
    print("it's a draw")

elif(score == 1):
    print("you win")

elif(score == -1):
    print("computer win")        
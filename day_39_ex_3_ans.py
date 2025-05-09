#create a program to capable of displaying question to the user like KBC(koun banega cororpati)....

#use list data type to store the question and answer......

#displaying the final amount the person is taking home after playing the game.
questions=[
    ["who is my best friend ?" , "deba" , "tarinee" , "debi", "miku", 4] , 

 ["java is a what type of language ?" , "programming language" , "simple language" ,"animal language" ,  "nothing" , 4],

 ["python is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] , 

 ["javascript is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] , 

 ["c is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] , 

 ["c++ is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] , 

 ["ruby is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] ,

 ["html is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] , 

 ["css is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] , 

 ["pearl is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] , 
 
 ["rust is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] , 
 
 ["cobal is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4] , 
 
 ["bash is what type of language ?" , "code language" , "programming language" , "simple language" , "nothing" , 4]
 
 ]


level=[1000 , 2000 , 3000 , 5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000]
money=0


i=0
for i in range(0 , len(questions)):
    question=questions[i]
    
    print(f"\n\nquestion for Rs. {level[i]}")
    print(question[0])#for question printing
    
    print(f"A.{question[1]}       B.{question[2]}")
    print(f"C.{question[3]}       D.{question[4]}")
    reply=int(input("enter the answer (1-4)"))
    if(reply == 2):
        print(f"correct answer and you won {level[i]}")
        if(i == 4):
            money=10000
        elif(i == 9):
            money=320000
            

    else:
        print("wrong answer")
        break   

print(f"your take home money is {money}")

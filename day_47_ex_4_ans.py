#in day 46 we are going slove a problem
#SECRET CODE LANGUAGE.......
#dsfarryhjkr si dsfoodgjkr
#..........................................................
#write a pyhton program to translate a message in to secrate code language. use the rules below to translate the normal  english into secret code languge..

#coding the message..
#if : the word contain atleast 3 charecter remove the first letter and append it at the end.
#now append three random charecter at the starting and the end

#else:
   #simply reverse the string..


#Decoding the message......
#if the word contains less than 3 charecters , reverse it

#else:
   #remove 3 random charecters from start and end .now remove the last letter and append it to the beginning

#your program should ask whether you want to code ar decode.... 
st=input("enter the message : ")
words=st.split(" ")
coding=input("enter 1 for coding or 0 for decoding : ")
coding=True if (coding=="1") else False
if(coding):
  nword=[]
  for word in words:
      if(len(word)>=3):
        r1="dsf"
        r2="jkr"
        stnew= r1 + word[1:] + word[0] + r2
        nword.append(stnew)
      else:
        nword.append(word[::-1])#reverse the  word....
  print(" ".join(nword))


else:
 nword=[]
 for word in words:
    if(len(word) >= 3):
        
        stnew= word[3:-3]#remove 3 charecter from first and last
        stnew=stnew[-1] + stnew[:-1]
        nword.append(stnew)
    else:
        nword.append(word[::-1])
print(" ".join(nword))




        
    
   

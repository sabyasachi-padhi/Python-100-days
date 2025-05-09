#in day 32 we are learn about set method........
s1={1,2,5,6}
s2={3 , 6 , 7}
#print(s1.union(s2))#union method merge the two set.....this a new set
#s1.update(s2)#now s1 is update........

# print(s1.intersection(s2))# this method wiil print intersection of the two set. mean the value which is common in two set in this case 6 is ans..........
# s1.intersection_update(s2)# now s1 value is update with common value between s1 and s2 ......
# print(s1 , s2)

# print(s1.symmetric_difference(s2))#in this method it will be print diffrence between s1 - s2 ......it will be not print common values

# s1.symmetric_difference_update(s2)
#print(s1 , s2)# now  s1 value is update.......

# print(s1.difference(s2))#this method print only items that are only present in the original set and not in both the set.....

# s1.difference_update(s2)
# print(s1 , s2)#now s1 value is change......with diffrence value.....

#SET METHOD IN BUILT-METHOD.............

print(s1.isdisjoint(s2))# it return false if there are any common element are present......

print(s1.issuperset(s2))
print(s2.issubset(s1))

s1.add(10)
print(s1)

# s1.remove(10)# this method raise an error.....if the element are not present in the set.....
# print(s1)

# s1.discard(10)
# print(s1)

# s1.pop()
# print(s1)

#del s1 # delete entier set....
#print(s1)

# s1.clear()#delete all the element from the set.....
# print(s1)

if 1 in s1:
    print("1 is present")







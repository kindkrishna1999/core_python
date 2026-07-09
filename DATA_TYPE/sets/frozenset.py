# frozen set: a frozen set is an imutalble (unchangable) set in python whose elements
# cannot be added , removed, or modified agter creation
# example 
# they on list tuple or string
# when we write element inside frozenset then it must be string, list, tuple etc

# myfruit = frozenset({"saroj",1,"ram","orange"})
# print(myfruit)
# print(type(myfruit))                #output: frozenset({'orange', 1, 'ram', 'saroj'})

# num = frozenset({"saroj"})
# print(num)          #frozenset({'saroj'})


# lst = frozenset(["saroj",1,2,"orange"])
# print(lst)              #frozenset({1, 2, 'orange', 'saroj'})

# tup = frozenset((1,2,3,"ram"))
# print(tup)                  #frozenset({1, 2, 3, 'ram'})



###############question####################
# question 1
# given set is 
details = {1,"saroj","ktm"}
details.add(50)
print(details)

#question 2 : 
# wap to your 3 friends name as input from user, and finally aadd them into the set named"friends.
# not using add() function and also check its data type.

friends = set()
friend1 = input("enter 1 friend:  ")
friend2 = input("enter 2 friend:  ")
friend3 = input("enter 3 friend:  ")
friends.add(friend1)
friends.add(friend2)
friends.add(friend3)
print(friends)

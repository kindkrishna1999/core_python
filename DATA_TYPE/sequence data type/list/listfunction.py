#####################1 append()###############

# syntax: varName.append(value)
# it adds the elements in the list.

# lst = ["apple","orange","car"]
# print(lst.append("elephant"))               #add any datatype in the function. in the time of print add the first variable where you create the list.
# print(lst)


# lst = ["apple","orange","car"]
# v = lst.append("elephant")      
# print(lst)

############################### 2. romove    ##########
#it removes the elements or value from the list.
# numList = [10,50,70,80,90,100]
# print(numList.remove(10))
# print(numList.remove(90))
# print(numList)

######################3. pop##############
#it remove the value by using index number      #in term of index [0123] =10,50,70,80,90,100
numList = [10,50,70,80,90,100]
print(numList.pop(1))
print(numList.pop(3))
print(numList)

######################## 4.   extend##############
#it add the one of the list value into another entended list.

# it add the datatype on lst 1 from lst 2
# lst1 = [1,2]
# lst2 = [3,4]
# print(lst1.extend(lst2))
# print(lst1)

# animal = ["cow","dog"]
# plant = ["herbs","shrubs"]
# print(plant.extend(animal))
# print(plant)


###################5. clear#################
# it clears the list all Elements values in the brackets.
#syntax: varName.clear(data)
# numList = [10,50,70,80,90,100]
# print(numList.clear())
# print(numList)

# fruits = ["apple", "orange", "dragonfruit"]
# print(fruits.clear())
# print(fruits)


##############6. count ##############

# in the list, the function execution the how many number of individual in the list , it help to count the single individual number in the list.
# numList = [10,50,60,80,90,50,20,30,20,20,30]
# print(numList.count(20))        #output:::::::::3 [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30]
# print(numList.count(50))        #output:::::::::2 [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30]
# print(numList)                  


#################7. insert #####################
# it will put the value of index in the list where (1,40) where you can see in the example you can see that in the index of 1 from the list it will change the 50 to 40.
#it keep the value in provide index number.
#syntax: varName.insert(indexnumber, value)
# numList = [10,50,60,80,90,50,20,30,20,20,30]
# numList.insert(1,40)
# numList.insert(4,40)
# print(numList)

################# 8. sort ##########################
#it help to arrange the data inside the list in asscending order.

# numList = [10,50,60,80,90,50,20,30,20,20,30]
# # numList.sort()
# # print(numList)

# print(numList.sort())
# print(numList)

###################### 9 reverse############
#it just the reverse from backword from the list.
# numList = [10,50,60,80,90,50,20,30,20,20,30]
# numList.reverse()
# print(numList)                  #output:[30, 20, 20, 30, 20, 50, 90, 80, 60, 50, 10]


#################### 10 sort with descending order #############
#it will reserve with descending order inside the list.
#syntax:: varName.sort(reverse=True)
# numList = [10,50,60,80,90,50,20,30,20,20,30]
# numList.sort(reverse=True)
# print(numList)                      #output::[90, 80, 60, 50, 50, 30, 30, 20, 20, 20, 10]



################ 11. copy ####################
# it help to copy the list as it is. or it help to duplicate the list.
# numList = [10,50,60,80,90,50,20,30,20,20,30]
# numList.copy()
# print(numList)              # output [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30]


######################### 11. min() #############################
# syntax: function (parameter) = (min(variable))
# numList = [10,50,60,80,90,50,20,30,20,20,30]
# print(min(numList))                             #not used . in the min becauses it allow or accept agrument.

########################12. max()#####################

# numList = [10,50,60,80,90,50,20,30,20,20,30]
# print(max(numList))                             #not used . in the min becauses it allow or accept agrument.

# ##################### 13. sum()#################
# numList = [10,50,60,80,90,50,20,30,20,20,30]
# print(sum(numList))                             #not used . in the min becauses it allow or accept agrument.and

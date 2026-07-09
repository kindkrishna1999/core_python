############ 1. add()################### it addds the elements inside the set
# myset = {1,55.5,"ram","sita"}
# myset1 = {"orange","apple"}
# myset.add(5)
# print(myset)  



##########2. update################
# it update the set balue by providing another set.
# print(myset.update({"krishna"}))
# print(myset)

# myset.update(myset1)
# print(myset)  #{1, 'ram', 'orange', 'sita', 'apple'}

############ 3. remove()###################
# it removes the elements inside the set.
# myset.remove(55.5)
# print(myset)        #{1, 'sita', 'ram'}

############ 4. discard()###################
# it also remove the element but it doesn,t throw error while element not found inside the set
myset = {1,55.5,"ram","sita"}
myset1 = {"orange","apple"}
# myset.discard("ram")
# print(myset)
# myset1.remove("apple")
# print(myset)
# myset.update(myset1)
# print(myset)

############ 5. pop()###################
# it removes any allue from the set by randomly.
# myset = {1,55.5,"ram","sita"}
# myset1 = {"orange","apple"}
# myset.pop()
# print(myset)            #output {'sita', 'ram', 55.5}

############ 6. clear()###################
# it removes all the elements indise the set.
# myset = {1,55.5,"ram","sita"}
# myset1 = {"orange","apple"}
# myset.clear()
# print(myset)        #output:set()


############ 7. union()###################
#it contain all the elements inside two sets.
# myset = {1,55.5,"ram","sita"}
# myset1 = {1,55.5,"orange","apple"}
# print(myset.union(myset1))
# print(myset | myset1)                     #(|) it is symbol of operator
# output {1, 'ram', 'apple', 55.5, 'sita', 'orange'}
# 

############ 8. intersection()###################
# it contain only common elemets from two sets.
# myset = {1,55.5,"ram","sita"}
# myset1 = {1,55.5,"orange","apple"}
# print(myset.intersection(myset1))       #{1, 55.5}
#print(myset.intersetion(myset1))
# print(myset&myset1)

################## 9. difference #############
# if two set is given then first difference from other. so it contain only first set element and removes all the value insede set.
# myset = {1,55.5,"ram","sita"}
# myset1 = {1,55.5,"orange","apple"}
# print(myset.difference(myset1))         #output {'ram', 'sita'}



#################symmetric difference###################
myset = {1,55.5,"ram","sita"}
myset1 = {1,55.5,"orange","apple"}          #(AUB)-(A∩B)
print(myset.symmetric_difference(myset1))           #OUTPUT: {'orange', 'ram', 'apple', 'sita'}

student = {
    "name":"krishna",
1:"id11",
55.55:"weight",
"age":"27",
"gender":"male",
"marks":[20,40,60,80,],
}

########################### 1.keys #######################
# print(student.keys())
#output: dict_keys(['name', 1, 55.55, 'age', 'gender', 'marks'])
#syntax: var.keys()

########################### 2. values #######################
# print(student.values())
#output: dict_values(['krishna', 'id11', 'weight', '27', 'male', [20, 40, 60, 80]])
# syntax: var.values()

########################### 3. items #######################
# print(student.items())
#output: dict_items([('name', 'krishna'), (1, 'id11'), (55.55, 'weight'), ('age', '27'), ('gender', 'male'), ('marks', [20, 40, 60, 80])])
#output as tuple form. it gives the key value paris in a tuple form and separatd with comma,   .
# syntax: var.items()

########################### 4. get #######################
# print(student.get("name"))          #output krishna @used quatation
# print(student.get(55.55))           #output weight  @not used quatation
#it access teh key value using get method(function)
# syntax: var.keys("key")

########################### 5. update #######################
# simple method
# student["name"] = "krishna"
# print(student)
# syntax: dic["key"]="value"

# update method: 
# student.update({"name":"ram"})
# print(student)
# #  output:          only one can update             {'name': #'ram'#, 1: 'id11', 55.55: 'weight', 'age': '27', 'gender': 'male', 'marks': [20, 40, 60, 80]}
# it updates the values of respected key.
# syntax: var.updates({"key":"value"})
# it updated the vlues of respected key if found, if not found then it will add the key and value at the end if dictonary.


########################### 6. clear #######################
#it removes all the key and value pair inside the dictonary.
# print(student.clear())          #output: none
# student.clear()
# print(student)                  #output: {}
# syntax: dict.clear()
########################### 7. setdefault #######################
# condition
#  student.setdefault({"name":"ram"})
# print(student)
# output :  student.setdefault({"name":"ram"})
    # ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^

#if the key is found then it show its default value, if not found then it add extra key value pair
# student.setdefault("address","none")
# print(student)              #{'name': 'krishna', 1: 'id11', 55.55: 'weight', 'age': '27', 'gender': 'male', 'marks': [20, 40, 60, 80], 'address': 'none'}
# syntax: dict.setdefault("key or value")
# print(student.setdefault("address"))            #output: none


########################### 8. pop #######################

# student.pop("name")
#                  #output:   {1: 'id11', 55.55: 'weight', 'age': '27', 'gender': 'male', 'marks': [20, 40, 60, 80]}
# student.pop(55.55)          #output:    {1: 'id11', 'age': '27', 'gender': 'male', 'marks': [20, 40, 60, 80]}
# print(student) 
# syntax: dict.pop()


########################### 9. popitems #######################
# it removes the last key-value from the dictonary
# student.popitem()
# print(student)          #output:  {'name': 'krishna', 1: 'id11', 55.55: 'weight', 'age': '27', 'gender': 'male'}
# syntax: var.popitem()

########################## differnt between error and none###############
#none
# print(student.get("address", "word not found"))
#output:   none
#it gives non fi key is not found

#error
# print(student["address","word not found"])
# # output :  print(student["address","word not found"])
#           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# KeyError: ('address', 'word not found')
#it throws ite error if key is not found.


#append is used for list

######################################### tuple to list######################

# student = {
#     "name":"krishna",
# 1:"id11",
# 55.55:"weight",
# "age":"27",
# "gender":"male",
# "marks":[20,40,60,8],
# }

# print(student.get("marks"))
# text = student.get("marks")
# print(text)
# text = list(student.get("marks"))
# text.append(50)
# print(text)
# student["marks"] = tuple(text)
# print(student)
# print(student.get("marks"))


# Dictionary: A dictionalry is a built-in data type in python that stores a collection of data in key and value pairs.
# each key si unique and is used to access its correspoinding value.
# it is mutable, ordered , and dont allow duplicate keys,
#  Dictionary is created by culy bracket{} and data (key vlaue pair is) seperated by comma","
#  syntax:
#  dic_var = {
#       key1"value1,
#       key2"value2,
#       key3"value3,
#  }
#  Note"
#   key must be unique and immutable data type.


# myDict = {
#     "name":"krishna kumar pariyar",
#     "class":"master degree in public administrtion",
#     "age": "27 years olds",
#     1:"2020d",
#     80.89:"weight",
# }
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())
# print(myDict.get("age"))
# myDict["age"] = ["29 years olds"]

# updateDict = {
#     "location": "Signamangal, Kathmandu"
# }
# myDict.update(updateDict)
# print(myDict)


# while wiriting key and value name then use double or single quotes..
# student = {
#     "name":"krishna",
# 1:"id11",
# 55.55:"weight",
# "age":"27",
# "gender":"male",
# "marks":[20,40,60,80,[2,4,6,[5,5,5,5,5,55]]],
# }
# print(student["name"])    # krishna          #access key value of name only.
# print(student[1])           #id11
# print(student[55.55])       #weight
# print(student["age"])                       #27
# print(student["gender"])                    #male
# print(student["marks"])                     #[20, 50, 90]
# student["age"] = "22"
# student["marks"].append(100)                #add append syntax used
# student["marks"][2]=90                      #index and change or number
# student[55.55] = "tree_height"              #replace
# del student["name"]                         #delet
# del student["marks"][2]
# print(student["marks"][4][3][3])               #change the number inside the list 
# print(student)                                #it access all the key and value of given data inside the dictionary:
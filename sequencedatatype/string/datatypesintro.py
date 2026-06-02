# data types in python define the type of value a variable can store.
# they tell the computer wherer the data is a number, text , list, etc
# type of data


##############1. immutable data types (cannot be changed after creation)###############
# 1.int, 
# 2.float, 
# 3.str, 
# 4.tuple 
# 5.and boolean


###############2 mutable data type: it is the type of data where it will be change after creation)
# 1. list, 
# 2. dict 
# 3. and set



# memeory interning  :   it removes the duplication of value and store in single memeory location
# example
a=5
b=5
# print(id(a))  #140720662759200
# print(id(b))        #140720662759200            #stay in same memory base
# print(a)
# print(b)


# string immutability check::########

# name = "krishna"             # replace but didnt change
# # print(name.index("k"))              #NameError: name 'name' is not defined
# # then if you write 
# print(name[0])   #k
# # name[0]="i"



# lst=["saroj" , "ram",  "hari"]
# print(lst[0])
# lst[0]=["krishna"]
# print(lst)                      #replace and change both

#raw strings (r)   #############it skip the escape character and print as it as normal string
# syntax: r"string with escape character(\)"
# name="he\tllo"
# print(name)         #he      llo
# name = r"hel\tlo"
# print(name)         #hel\tlo





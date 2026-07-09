# #Tuple:
# collection of data (elements or data items) which is immutable, ordered, and allow duplicate elements.
# tuple s generally created by small bracket() but it is optional , and elements of tuple are seperated by comma.
# for example:
#     a=5,
#     we can store different tupes of data together in a tuple.
#     for exampe: 
#         details = (1,"saroj",26,"60.50", "kathmandu",true)


#################### creating tuple###############################
# mytuple = ()
# mytuple = tuple()
# print(mytuple)

##################immutable check##############
# details = (1,"saroj",26,"60.50", "kathmandu", True)
# details[2] = "krishna"
# print(details)          #### output: TypeError: 'tuple' object does not support item assignment


#FUNCTION#

#############################################1. CONCATINATION(+) PROPERTY#########################################
# fruits = ("apple","orange","pineapple","mango","banana","grapes","dragonfruits")
# colors = ("red","black","green")
# # text = fruits + colors
# print(text)
# #or
# print(fruits+colors)            #output: ('apple', 'orange', 'pineapple', 'red', 'black', 'green')



####################################### 2. access value of tuple by using INDEX ###############################################
# print(fruits[2])        #OUTPUT: pineapple



########################## 3. slicing ######################
# syntax: var[start: end: step]
# fruits = ("apple","orange","pineapple","mango","banana","grapes","dragonfruits")
# print(fruits[1:3])              #('orange', 'pineapple')
# print(fruits[-4:-2])            #('mango', 'banana')

#METHOD OR FUNCTION#


####################1 COUNT ############################

# 1. count()
# fruits = ("apple","orange","pineapple","mango","banana","grapes", "grapes","dragonfruits")
# print(fruits.count("grapes"))


# 2. index()
#it gives the index of searched or provided data.
# print(fruits.index("orange"))


# 3. swaping 
# a = "apple"
# b = "orange"
# v = a
# a = b
# b = v
# print("a is : ",a)
# print("b is : ",b)
# print(f"a is {a}")
# print(f"b is {b}")
# print(f"a is {a} \nb is {b}")

# 4. unpacked tuple
#assign the values of tuple in different variable in a single statement respectively.
a,b,c = (1,2,3)
print(a)            #1
print(b)            #2
print(c)            #3

#variable takes all the values reamaining in the tuple in the form of list.
d,e,*f = (4,5,6,7)
print(d)    #4
print(e)    #5
print(f)    #[6, 7]



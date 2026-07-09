###############################################list#######################################
#collection of data elements or data items which is mutalble, ordered, and allow duplicate elements.
# list is created by [ and elements of list are seperated by comma.]
# we can create list using list()function if data is in string, tuple, interger etc.

# syntax:
# list("datatype")
# str = "saroj"
#print(list(str))

##########################
# str = "saroj"
#print(list(str))                       #convert into string

#text = (1,2,3)
#print(list(text))

# print(list((1,2,3,4)))                  #tuple need different bracket inside the another bracket called list.

#print(list("krishna"))

# property of list

# lst = ["apple" , "orange"]              #mutability check on list property.          
# lst[1]="mango"
# print(lst)

# lst1 = [1,2,3,4,5,6,7,8,9]
# lst1[4]=0
# print(lst1)

# lst = ["apple" , "orange" , "apple" , "orange"]         #allow the duplication 
# print(lst)

###########################################access llist emenent y using indexing
# syntax: varName[indexing number]



# lst = ["apple" , "orange" , "ram" , "orange"]       #access 
# print(lst[2])

# mixing = ["apple","mango",1,55,5,"shyam","hari","toyta","suzuki"]

#print 55.5,shyam,toyta,apple using indexing

mixing = ["apple","mango",1,55.5,"shyam","hari","toyta","suzuki"]

a = mixing[3]
print(a)

b= mixing[4]
print(b)

c = mixing[6]
print(c)

d = mixing[0]
print(d)

print(a,b,c,d)





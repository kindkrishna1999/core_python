#  string function is a tool or method that helops to manipulate, modify, or analyze text. it is a way 


# 1...................case conversion (upper lower tiltle capatilize)
#                       a.................uper case conversion: it converts all letters into upper case (fully capital)
                        # syntx: variable name.upper()

# name = "arishna"
# text = name.upper()
# print(name.upper())
# print(text)
# print (name)

#print(name)
# name.upper()
# print(name)

                    #  b....................... lower case: it converts word alll lettters into lowercase small alphabetic form
                        # syntx: variablename.lower()
                        # reason behind two bracket is one for print and other for lower function.

# collegeName = "xAVier"
# # print(collegeName.lower())

# gender = "MALE"
# print(gender.lower())             #male


                                # c........................title():    it converts every words inside the string where every first letter of word will be capital and other same word in samll.
                                #  syntax: variableName.title()

# collegeName = "my name is krishna kumar pariyar"
# collegeName.title()
# print(collegeName.title())                #My Name Is Krishna Kumar Pariyar



                            # 2...........................capatilize function : it convert first word first letter and others remains in lowercase
                            # syntax: variableName.capitalize()     only first work other wont work, other in lower case
# collegeName = "my name is krishna kumar pariyar. i am 25 years old."
# collegeName.title()
# print(collegeName.capitalize())             #My name is krishna kumar pariyar. i am 25 years old.


# question: write a program to capitalize only the first letter of the string" python is fun.
# name = "python is fun"
# print(name.capitalize())


# take the five actor name as input and then check its data type and also take age in interger and then print it in console.
# after that convert name in uppercase, lowercase, capatalize, title. RESULT print in console

# actor1 = input("enter the name of actor")
# actor1Age = int(input("enter the age"))
# print(actor1)
# print(actor1.upper())
# print(actor1Age)                                       #actorName is a argument
# print(type(actor1))
# print(type(actor1Age))



# actor2 = input("enter the name of actor")
# actor2Age = int(input("enter the age"))
# print(actor1)
# print(actor2.upper())
# print(actor2Age)                                     
# print(type(actor2))
# print(type(actor2Age))



# actor3 = input("enter the name of actor")
# actor3Age = int(input("enter the age"))
# print(actor3)
# print(actor3.upper())
# print(actor3Age)                                     
# print(type(actor3))
# print(type(actor3Age))



# actor4 = input("enter the name of actor")
# actor4Age = int(input("enter the age"))
# print(actor4)
# print(actor4.upper())
# print(actor4Age)                                     
# print(type(actor4))
# print(type(actor4Age))



# actor5 = input("enter the name of actor")
# actor5Age = int(input("enter the age"))
# print(actor5)
# print(actor5.upper())
# print(actor5Age)                                     
# print(type(actor5))
# print(type(actor5Age))



# question : take a username from the user as input then check thier case if they hit uppercase then convert it into lowecase
# if hit lowercse then convert into uppercase

# name = input("enter the name of: ")
# print("upper:", name.upper())
# print("lower:" , name.lower())
# print("upper", text.upper())
# print("lower", text.lower())

# name = input("enter the name of :")
# print


                    # 2. CHECKING METHOD: RETURN TRUE/ FALSE: ISALPHA, ISDIGIT, ISALNUM, ISSPACE, ISLOWER, ISUPPER
# in checking method we check the real string type like it may be ISALPHA, ISDIGIT, ISALNUM, {ALBHABET+NUMBER-->COMBOO},ISPACE(), ISLOWER(),ISUPPER()
# THEN ITS OUTPUT IS TRUE OTHERWIESE FALSE.

# a = " "
# print(a.isspace())



                        # a. ...................isalpha checks the string in alphavetic form if alphabetic then active true otherwise false

# text = "hello World"   #due to having the space it read space also so, we can conclude that it shows the result of false, it check only one word 
# print(text.isalpha())

# text = "helloWorld"   
# print(text.isalpha())   #true

# num = "123"
# print(num.isalpha())   #false


# symbol = "@"
# print(symbol.isalpha())

                            # b: isdigit(): it checks the numerical data. if data is numerical then active(true) other wiese false

# num = "123.06"
# print(num.isdigit())                #it always takes integer value so it shows the result as false.


# number = "1234"
# print(number.isdigit())

# number = "-1234"
# print(number.isdigit())     #it shows the result as false due to symbol shows as minus   




                        #c .........................isalnum() it check both alphabet, number or combination of both then, it gives true.

# text = "abc123"
# print(text.isalnum())

# num = "123456"
# print(num.isalnum())

# word = "python"                 #if there is any space or word, special character came after the space it will be false , even inside the word if there is any special character it will turn into false as a result.
# print(word.isalnum())



                                #d...................isspace(): check the is there any space then it show true otherwise it show the result as false, but if there is any space between word then it show the false.

# a=""
# print(a.isspace())    # result=false

# a=" "
# print(a.isspace())

# name="krishna kumar"
# print(name.isspace())



#                                 #islower(): this checks the string is in lowercase
# name="saroj"
# print(name.islower())

# make="Car"
# print(make.islower())


                            # f: ..................isupper(): if the each alphabhet in the word are captial then it give true but any one of the character of alphabhet is in small letter then it gives a false

# name="Saroj"
# unsername="SAROJ"
# actor="doN"
# print(name.isupper())
# print(unsername.isupper())
# print(actor.isupper())            







#####################3. searching method(find(),index() start from 0 to 9...,count())################
                                    # a...........(find(): it help to serach the location of character of in the word and find the location of the character of position.


# fruit="avvvvvpple"
# eat=fruit.find("p")
# print(eat)

# address="signamangalwardno31"
# location=address.find("3")
# print(location)
#                                 #b...........index():  # index value : omdex value os always start with zero(0)


# address="kathmandu"
# print(address.index("u"))


                            #c..............count(): it count the all of charcter of the give word in the string.
# address="kathmaaaaaaandu"
# print(address.count("a"))

# question 
#1. take the word "Encyclopedia" amd check "cl", "ed", "de" using find function and write output
# 3 , count a,e,m , t,o
ssg = "Hello This is Deepak from Mahendranager"
print(ssg.count("a"))
print(ssg.count("e"))
print(ssg.count("m"))
print(ssg.count("t"))
print(ssg.count("o")) 



word="Encyclopedia"
print(word.find("cl"))
print(word.find("c"))
print(word.find("de"))
print(word.find("ed"))

print(word.index("cl"))
print(word.index("c"))
print(word.index("de"))
print(word.index("ed"))
























































# class work









































# ==============Practice Questions for Case Conversion Methods in Strings=================
# Q1.Write a Python program to convert the string "hello world" into uppercase.

# name = "hello world"
# print(name.upper())


# # Q2.Convert the string "PYTHON PROGRAMMING" into lowercase.
# name = "PYTHON PROGRAMMING"
# print(name.lower())

# # Q3.What will be the output?
# s = "hello python"
# print(s.title())   #output will be (h CHANGE IN CAPATIAL)
  


# # Q4.Differentiate between title() and capitalize() with example.
# # title works as : only first letter of word as upper but capitalize(function acts as whole letter of words as uppercase)

# # Q5.Write a program to capitalize only the first letter of the string "python is fun".
# name = "python is fun"
# print(name.title())


# # Q6.What will be the output?
# s = "hELLO wORLD"
# print(s.capitalize())           #Hello world


# # Q7.Write a program to take user input as (name,collegeName,address,favouritePlayer,FavouriteGame) and convert it into:
#     # •	uppercase 
# # name = input("enter the name:")
# # collegeName = input("enter the name of the college:")
# # address = input("enter the address:")
# # favouritePlayer = input("enter the favourite player you like:   ")
# # FavouriteGame = input("enter the game you like the most:") 
# # print(name.upper())
# # print(collegeName.upper())
# # print(address.upper())
# # print(favouritePlayer.upper())
# # print(FavouriteGame.upper())


# # #  •	lowercase 
# # name = input("enter the name:")
# # collegeName = input("enter the name of the college:")
# # address = input("enter the address:")
# # favouritePlayer = input("enter the favourite player you like:   ")
# # FavouriteGame = input("enter the game you like the most:") 
# # print(name.lower())
# # print(collegeName.lower())
# # print(address.lower())
# # print(favouritePlayer.lower())
# # print(FavouriteGame.lower())


# # Q8.What will be the output?
# s = "123abc"
# print(s.upper())   #output 123ABC


# # Q9.Correct the following string using proper case (title case):
# s = "welcome to nepal"
# print(s.title())


# # Q10.Predict the output:
# s = "python programming"
# print(s.capitalize()) #Python programming
# print(s.title())    #Python Programming



# text = input("enter your name: ")
# print(text.swapcase())              #swapcase is the function that used in upper and lower case where it easy swap or change upper into lower or vice-versa.




# name = input("enter the name:")
# collegeName = input("enter the name of the college:")
# address = input("enter the address:")
# favouritePlayer = input("enter the favourite player you like:   ")
# FavouriteGame = input("enter the game you like the most:") 
# print(name.upper())
# print(collegeName.upper())
# print(address.upper())
# print(favouritePlayer.upper())
# print(FavouriteGame.upper())


# #  •	lowercase 
# name = input("enter the name:")
# collegeName = input("enter the name of the college:")
# address = input("enter the address:")
# favouritePlayer = input("enter the favourite player you like:   ")
# FavouriteGame = input("enter the game you like the most:") 
# print(name.lower())
# print(collegeName.lower())
# print(address.lower())
# print(favouritePlayer.lower())
# print(FavouriteGame.lower())







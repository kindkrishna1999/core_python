# #append 50 and 60 to the list

# num1 = [10,20,30]
# print(num1.append(50))
# print(num1.append(60))
# print(num1)


# # Q7 Append 5 and 15 to the list:
# # num_list6 = [1, 2, 3]

# num2= [1,2,3]
# print(num2.append(5))
# print(num2.append(15))
# print(num2)

# # Q8 Append 100 and 200 to the list:
# # num_list7 = [25, 50, 75]

# num3= [25,50,75]
# print(num3.append(100))
# print(num3.append(200))
# print(num3)

# # Q9 Append "Mango" and "Apple" to the list:
# # fruits_list8 = ["Banana", "Orange"]

# fruits = ["Banana", "Orange"]
# print(fruits.append("mango"))
# print(fruits.append("apple"))
# print(fruits)



# # Q10 Append 999 and 888 to the list:
# # num_list9 = [111, 222, 333]

# num4= [111,222,333]
# print(num4.append(999))
# print(num4.append(888))
# print(num4)

#qn.2 print hari and shyam in console  and add using append elephant,sunflower["apple", "banana","ram",1, "shyam",55.5, "hari"]

# lst = ["apple", "banana","ram",1, 55.5,"hari","shyam"]
# v = lst[5]
# a = lst[6]
# print(lst)
# print(lst.append("elephant"))
# print(lst.append("sunflower"))
# print(lst)


# Q12 Write a program to add your 3 favourite players in a list using append() function.
#note: take 3 favourite players as input from user.
# player = [("name of the three player are: ")]
# player1 = input("1 player")
# player2 = input("2 player")
# player3 = input("3 player")
# player.append(player1)
# player.append(player2)
# player.append(player3)
# print(player)

#another method
# players = [input("enter fitst player name: ")]
# players.append(input("enter secodn palyer name"))
# players.append(input("enter third palyer name"))
# print("plaer list:",players)

#

# Q1. Full Name Split Program

# Write a Python program that:

# Takes full name from user
# Uses split()
# Prints first name and last name separately

# firstName: sushil
# LastName : singh

#answer
# firstName = input("enter your first name:  ")
# lastName = input("enter your first name:  ")
# print(firstName.split("firstName"))
# print(lastName.split("lastName"))
# print(firstName)
# print(lastName)

# Q2. Email Analyzer Program

# Write a Python program that:

# Takes email from user
# Uses split("@")
# Prints username and domain name separately

# email = input("enter the full email id: ")
# text= email.split("@")
# print(text)
# print("username", text[0])
# print("domain name", text[1])

# Q4. Word Join Program

# Write a Python program that:

# Takes 3 words from user
# Stores them in list
# Uses join()
# Joins all words with space

# text1 = input("first word")
# text2 = input("second word")
# text3 = input("third word")
# v = text1 + text2 + text3
# print(v)


# Q5. CSV Data Split Program                    #######################

# Write a Python program that:

# Takes comma-separated values from user
# Uses split(",")
# Prints each value separately

# name = input("enter your name: ")
# print(name.split(","))
# print(name)


# Q1. Clean Name Input Program (strip)
# Write a Python program that:
# Takes a name from user with extra spaces
# Removes spaces from both sides using strip()
# name = input("enter the name: ")
# print(name.strip())
# print(name)

# Q2. Remove Left Side Spaces (lstrip)
# Write a program that:
# Takes input with left spaces
# Removes only left side spaces

# name = input("enter the word: ")
# print(name.lstrip())
# print(name)

# Q3. Remove Right Side Spaces (rstrip)
# Write a program that:
# Takes input with right spaces
# Removes only right side spaces

# name = input("enter the word: ")
# print(name.rstrip())
# print(name)


# Q4. Username Cleaner (strip + length)
# Write a program that:
# Takes username with extra spaces
# Removes spaces using strip()
# Prints cleaned username and its length



# Q1. Remove prefix from website

# Given string: "www.facebook.com"
# Apply removeprefix("www.")

# name = "www.facebook.com"
# print(name.removeprefix("www."))
# print(name)

# Q2. Remove suffix from domain

# Given string: "google.com"
# Apply removesuffix(".com")

# website = "google.com"
# print(website.removesuffix(".com"))


# Given string: "Mr. Saroj"
# Apply removeprefix("Mr. ")

# Result: Saroj
# name = "Mr. Saroj"
# print(name.removeprefix("Mr."))


# Q4. Remove file extension

# Given string: "notes.txt"
# Apply removesuffix(".txt")

# Result: notes

# name = "notes.txt"
# print(name.removesuffix(".txt"))
# print(name)

# Q5. Remove both prefix and suffix

# Given string: "www.python.org"
# Apply removeprefix("www.") and removesuffix(".org")

# Result: python
# name = "www.python.org"
# print(name.removeprefix("www."))
# print(name.removesuffix(".org"))
# print(name)
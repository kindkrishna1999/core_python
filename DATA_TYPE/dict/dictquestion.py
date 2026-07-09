
# details = {
#     "name":"deepak",
#     "age":26,
#     "address":"Mahendranagar,Nepal",
#     "weight":68.5,
#     "subjects":("English","Math","Science","Biology"),
#     "marks":[90,40,50,80,90,100],
#     "favPlayers":["Messi","Ronaldo","Neymar"] ,   
# }
# # print(details.get[90,40])
# print(details)
# details.get("subjects").clear()
# print(details)
# # Print the following output

# # Output:
# # Deepak
# # print(details["name"])
# # print(details["subjects"])
# # print(details["favPlayers"])

#EXTRA QUESTION#
# 1.	Create a dictionary with name, age, and city. Add a new key gpa.
# name = {
#     "name" : "krishna",
#     "age" : 26,
#     "city": "kathmandu",
# }
# print(name.update({"gpa":3.20}))
# print(name)             #output: {'name': 'krishna', 'age': 26, 'city': 'kathmandu', 'gpa': 3.2}

#	2. Create a dictionary and update the age from 22 to 23.
# name["age"] = 23
# print(name)             #output: {'name': 'krishna', 'age': 23, 'city': 'kathmandu', 'gpa': 3.2}

# 3.	Remove the city key from a dictionary.
# print(name.pop("city"))
# print(name)           #{'name': 'krishna', 'age': 26}

# 4.	Take a key from the user and display its value using get().
# data = {
#      "name" : "krishna",
#     "age" : 26,
#     "city": "kathmandu",
# }
# v = input("enter the word: ")
# print(data.get(v," not found your word"))  enter the word: age    output:26



# 5.	Add multiple new keys (email, phone) using update().
# v = {
#     "name" : "krishna",
#     "age" : 26,
#     "city": "kathmandu",
# }
# print(v.update({"email":"acb@gmail.com"}))
# print(v.update({"phone":9840341764}))
# print(v)                    #{'name': 'krishna', 'age': 26, 'city': 'kathmandu', 'email': 'acb@gmail.com', 'phone': 9840341764}


# 6.	Remove the last inserted item using popitem().
# print(v.popitem())
# print(v)            #{'name': 'krishna', 'age': 26, 'city': 'kathmandu', 'email': 'acb@gmail.com'}

# 7.	Copy a dictionary and add a new key in the copied dictionary.

v = {
    "name" : "krishna",
    "age" : 26,
    "city": "kathmandu",
}

a = v.copy()
a.update({"rollno":12})
print(a)












# 8.	Clear all records from a dictionary.

# print(v.clear())



# 9.	Create a dictionary using fromkeys() with keys:
# 10.	Use setdefault() to add a faculty key if it does not exist
# 11.	Add a new student to a nested dictionary.
# 12.	Update Hari's age from 21 to 22.
# 13.	Remove student s1 from the nested dictionary.
# 14.	Add GPA to student s1.
# 15.	Display only the age of student s2.
# 16.	Replace Ram's name with Shyam.
# 17.	Add a new subject key inside student s1.


# 18.	Create an employee dictionary and:
# Add salary 
# Update salary 
# Remove department
# 19. Create a product dictionary and:
# •	Add stock 
# •	Update price 
# •	Delete category
# k ={
#     "name":"bottle",
#     "price":100,
#     "category":"2 grade",
# }
# print(k)
# k["stock"] = "b"
# print(k)

# print(k.update({"price":40}))
# print(k)


# print(k.pop("category"))





# 20. Create a library dictionary and:
# •	Add author 
# •	Update book title 
# •	Remove publication year

# k = {
#     "a":"b",
#     "publication_year":2000
# }
# k["author"] = "krishna"
# print(k)

# print(k.update({"book title":"king"}))
# print(k)

# # print(k.pop("publication year"))
# # print(k)
# #####################delect command###
# del k["publication_year"]
# print(k)



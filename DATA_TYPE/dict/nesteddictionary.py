# # student = {
# #     "course" : "bsc it",
# #     "rollno1" : {
# #         "name" : "ram",
# #         "age" : 21
# #     },
# #     "name" : "sham",
# #     "age" : 31,
# # }
# # student.get("rollno1").update({"name":"krishna"})
# # print(student)


# # syntax: dic["key"]="value"

# # print(student.get("rollno1").get("name"))



student = {
"name": "Skm",                 
    "age": 22,                       
    "gpa": 3.85,                     
    "is_active": True,               
    "subjects": ("Python", "Django"),
    "(1,2,3,4)" : 95,

"details" : {
    "name":"Saroj",
    "age":26,
    "address":"Mahendranagar,Nepal",
    "weight":68.5,
    "subjects":("English","Math","Science","Biology"),
    "marks":[90,40,50,80,90,100],
    "favPlayers":["Messi","Ronaldo","Neymar"]       
}
}
# student.get("details").get("marks")[3]=120
# print(student.get("details").get("marks"))


# print(student.get("details").get("marks").append(10000))
print(student.get("details").get("subjects"))
# print(student.get("details").get("subjects"))
# print(student.get("subjects").append("chemistry"))



# print(student)
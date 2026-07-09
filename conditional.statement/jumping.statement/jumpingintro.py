#jumping_statements:
# jumping statements determine the execution the flow of code execution
# continue, break, pass


######################### break ###################
#it breaks the execution of program.
# lst = [1,2,3,20,40]
# for i in lst:
#     if i == 20:
#         break
#     print(i)
#     print("Hello World")


# lst = [1,2,3,4,5,6,7,8,9]
# for i in lst:
#     if i == 4:
#         break
#     print(i)


########################continue#################
# it continue the loop skiping the continue value.
# example
# lst = [1,2,3,40,20,40]
# for i in lst:
#     if i == 40:
#         continue
#     print(i)
#     print("Hello World")

    

# lst = [1,2,3,4,5,6,7,8,9]
# for i in lst:
#     if i == 4:
#         continue
#     print(i)

####################### pass######################
# it prints all the data inside the program. ( contional: skiping the given data from user)
# lst = [1,2,3,40,20,40]
# for i in lst:
#     if i == 1:
#         pass
#     print(i)

lst = [1,2,3,4,5,6,7,8,9]
for i in lst:
    if i == 4:
        pass
    print(i)
print("Hello World")
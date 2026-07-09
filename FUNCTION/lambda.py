#### lambda function####
# A LAMBDA function is small, anonymous function that does not hace name.

# we use lambda keyword to define lambda function.
# Syntax
# Lmvs PeMWRWEA: WZPEWAAION

# HERE, 
# parameters ==> one or More 
# but, 
# expression ==> only one
#  this expression os executed (runs) and return result.

 #example
# result = lambda a,b:a+b
# print(result(2,4))

#area of triangle
# area_of_triangle = lambda height,breath:(1/2)*height*breath
# print( "area of triangle is:",area_of_triangle(2,10))

# area_of_circle = lambda radius:3.14*radius*radius
# print("area of circle:",area_of_circle(8))

# eligible = lambda age: age >=18
# print("eligibilty",(x))
# x = (input("enter the age"))

Eligibility_criteria = lambda age: "eligible" if age>=10 else "not eligible"
age = int(input("enter your age::"))
print("Eligibility_criteria",Eligibility_criteria(age))         #function lai call garnu parni compulsory ho





################# question ####################
# Question 1: Library Fine Calculator
# A library charges fines for overdue books.
# Write a Python function calculate_fine(days_late) that applies the following rules:
# First 5 days: Rs. 2 per day
# Next 5 days: Rs. 5 per day
# More than 10 days: Rs. 10 per day for the remaining days
# The function should return the total fine.

# def pay_fine (leave_day):
    
#     fine = 0

#     if leave_day <=5:
#         fine = leave_day*2

#     elif leave_day <=10:
#         fine=(5*2)+(leave_day-5)*5

#     else:
#         fine = (5*2)+(5*5)+(leave_day-10)*10

#     return fine
# days = int(input("enter the leave days:  "))
# print("your leave day are", days , "and you need to fine rs",pay_fine(days))


# def pay_fine (leave_day):
    
#     fine = 0

#     if leave_day <=5:
#         fine = leave_day*2

#     elif leave_day <=10:
#         fine=(5*2)+(leave_day-5)*5

#     elif leave_day <=10:
#         fine = (5*2)+(5*5)+(leave_day-10)*10
#     else:
#         fine = (5*2)+(5*5)+(5*10-15)*15

#     return fine

# days = int(input("enter the leave days:  "))
# print("your leave day are", days , "and you need to fine rs",pay_fine(days))




        



# Question 2: Age Eligibility Checker Using Lambda function.

# A company wants to check whether a candidate is eligible to apply for a job.

# Write a lambda function that accepts a candidate's age and returns:

# "Eligible" if the age is 18 or above.
# "Not Eligible" otherwise.

# Example
# Input:
# Age = 20

# Output:
# Eligible

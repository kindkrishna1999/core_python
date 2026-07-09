# 
#  1. Conditional Statement[Sectional Statement/Desicion making statement]: [if, if-else, if-elif-else]
#        # These statements are used to check conditon, and decide(select) which block of code run.

#         # Types of Conditional Statement:
#             a. if:
#                 if statement is used to check condtion.
#                 if the conditon is true, then the code inside if block will run.

#                 syntax:
#                 if condition:
#                     #body(i.e. body will be executed(run) if the condition is true)


#             b. if-else:
#                 if-else statement is used to check condition.
#                 # if the condition is true, the code inside if block execute.
#                 # if the condition is false, the code inside else block execute.

#                 syntax:
#                 if condition:
#                     #body(i.e. body will be executed if the condition is true)
#                 else:
#                     #body(i.e. body will be executed if the condition is false)


#             c. if-elif-else:
#                 if-elif-else statement is used to check multiple conditions.

#                 #if statement check first condion.
#                 #elif statement check next condition.
#                 #else statement execute when all condtions are false.

#                 syntax:
#                 if condition1:
#                     #body(i.e. body will be executed when condtion1 is true)
#                 elif condition2:
#                     #body(i.e. body will be executed when condtion1 is false and condition2 is true)
#                 elif condition3:
#                     #body(i.e. body will be executed when condtion1,condition2 are false and conditon3 is true)
                
#                 .................
#                 else:
#                     #body(i.e. body will be executed when all the condition are false)








#================================Examples of if statement ==============================
#example:
# a = 5
# b = 3

# if a>b:
#     print("Hello i am inside the if block")
#     print("k xa vai, kata xau")
#     print("a is greater than b")


# print("Hello i am outside the if block")
# print("hey funny boy....")


#example2:
# a = 20
# b = 3

# if a>b:
#     print("Hello i am inside the if block")
#     print("k xa vai, kata xau")
#     print("a is greater than b")
#     exit()


# print("Hello i am outside the if block")
# print("hey funny boy....")



#=========== exit(): exit() is used to terminate(exit) the program ================
# print("hello")
# print("where are you")
# exit()
# print("kdjdjd")
# print("kdkdkdkdkkdd")


#============ nested if or nested if-else: ============
#greatest among three numbers.
# a = 2
# b = 3
# c = 4

# if a>b:
#     if a>c:
#         print("a is greatest")

# if b>a:
#     if b>c:
#         print("b is greater")

# if c>a:
#     if c>b:
#         print("c is greater")





#  qn  find the greatest among three numbers.
#method-2:
# a = 2
# b = 3
# c = 4

# if a>b and a>c:
#     print("a is greater")

# if b>a and b>c:
#     print("b is greater")

# if c>a and c>b:
#     print("c is greater")





#========================== example of  if-else statement ======================
#program to find greater number
# a = 20
# b = 30

# if a>b:
#     print("Hello i am inside if block")
#     print("a is greater than b")
# else:
#     print("Hello i am inside else block")
#     print("b is greater than a")




#====================== example of if-elif-else =======================
#greatest among 3 numbers
# a = 2
# b = 3
# c = 4
# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
# c = int(input("Enter value of c: "))

# if a>b and a>c:
#     print("a is greatest")

# elif b>a and b>c:
#     print("b is greatest")

# else:
#     print("c is greatest")



#   Q.1  Take gender input from user.
#     Print "You are a boy" if user enter Male. otherwise print "You are a girl".

# gender = input("Enter your gender(male or female): ").lower()

# if gender == "male":
#     print("You are a boy")
# if gender == "female":
#     print("you are a girl")




# """
# # Q2. Take email and password from user.
# #     Print "Login successful" if email is "deepak@gmail.com", and password is "12345"
# #     otherwise print "Incorrect email or password"





# #print even numbers from 0 to 50 using while loop
 
# # i = 0

# # while i<51:
# #     if i%2 == 0:
# #         print(i)
# #     i = i+1


# #or
# # i = 0
# # while True:
# #     if i%2 == 0:
# #         print(i)
# #     i = i+1

# #     if i == 51:
# #         break


# #1. print even numbers from 0 to 50 using for loop

# # for i in range(0,51,1):
# #     if i%2 == 0:
# #         print(i)


# # for i in range(0,51,2):
# #     print(i)



# # for i in range(1,50,2):
# #     print(i)
# # for i in [1,2,3]:
# #     print(i)
# #     break


# # print("hello")


# for i in [1,2,3,4,5]:
#     if i%2==0:
#         break

# QUESTION 

# Write a program to check whether a number is positive or negative.

# number = int(input("Enter any number: "))

# if number >= 0:
#     print("positive")
# else:
#     print("negative")


# # Write a program to check whether a number is even or odd.
# number = int(input("Enter any number: "))

# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")
# # Write a program to find the largest of two numbers  by taking number from user.

# num1 = int(input("enter num1:   "))
# num2 = int(input("enter num2:   "))
# if num1>num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater")


# Write a program to find the smallest of two numbers.
# num1 = int(input("enter num first:   "))
# num2 = int(input("enter num second:   "))
# if num1<num2:
#     print("num1 is smallest")
# else:
#     print("num2 is smallest")

# Write a program to check whether a person is eligible to vote.
# eligible = int(input("enter the current age:   "))
# if eligible>+18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

# Write a program to check whether a student has passed or failed (pass marks = 40).

# student = int(input("enter your Math mark:   "))
# if student>=40:
#     print("you are pass")
# else:
#     print("you are fail")

# Write a program to compare two strings.

# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")

# if string1 == string2:
#     print("Both are equal.")
# else:
#     print("Both are not equal.")



# Write a program to check whether a number is divisible by 5.
# num = int(input("enter the number:  "))
# if num %5==0:
#     print("it is divisible by 5")
# else:
#     print("it is not divisible by 5")



# Find the largest among three numbers.
# num1 = int(input("enter any first number :   "))
# num2 = int(input("enter any  second number :   "))
# num3 = int(input("enter any third number :   "))
# if num1>num2 and num1>num3:
#     print("num1 is greater")
# elif num2>num1 and num2>num3:
#     print("num2 is greater")
# else:
#     print("num3 is greater")


# Find the smallest among three numbers.
# num1 = int(input("enter any first number :   "))
# num2 = int(input("enter any  second number :   "))
# num3 = int(input("enter any third number :   "))
# if num1<num2 and num1<num3:
#     print("num1 is smallest")
# elif num2<num1 and num2<num3:
#     print("num2 is smallest")
# else:
#     print("num3 is smallest")


# Check whether a number is divisible by both 3 and 5.
# num = int(input("enter the number:  "))
# if num %5==0 and num%3==0:
#     print("it is divisible by 5 and 3")
# else:
#     print("it is not divisible by 5 and 3")




# 1.Write a program to calculate grades based on marks.
# 90–100 : A
# 80–89  : B
# 70–79  : C
# 60–69  : D
# Below 60 : F
# student = float(input("enter your marks:  "))
# if student >= 90 and student <= 100:
#     print("your grade is: A ")
# elif student>= 80:
#     print("your grade is: B ")
# elif student>= 70:
#     print("your grade is: C ")
# elif student>= 60:  
#     print("your grade is: D ")
# else:
#     print("your are fail: F")
    
# 2. Write a program to display the day of the week based on a number (1–7).

# week = int(input("enter the number to find the day:  "))
# if week ==1:
#     print("day of week is: Sunday")
# elif week ==2:
#     print("day of week is: Monday")
# elif week ==3:
#     print("day of week is: tueday")
# elif week ==4:
#     print("day of week is: Wednesday")
# elif week ==5:
#     print("day of week is: Thursday")
# elif week ==6:
#     print("day of week is: Friday")
# elif week ==7:
#     print("day of week is: Saturday")
# else:
#     print("invaid number to find the week day.")


# 3. Write a program to classify a person's age.
# 0–12 : Child
# 13–19 : Teenager
# 20–59 : Adult
# 60+ : Senior Citizen

# age = float(input("enter your current age: "))
# if age >=0 and age <=12:
#     print("you are consider as :child")
# elif age >=13 and age <=19:
#     print("you are consider as :teenager")
# elif age >=20 and age <=59:
#     print("you are consider as :Adult")
# elif age <=60 and age <=100:
#     print("you are consider as Senior Citizen")
# else:
#     print("invalid number")


# 4. Create a simple login system with three attempts.
# usr = "krishna"
# psw = 123               #yeti string put garapachi you can easily put number or alphabet

# username = input("enter your username: ")               
# password = int(input("enter your password"))
# if username == usr and password == psw:
#     print("login successful")
# else:
#     print("invalid or password")

############### while
# username = "krishna"
# password = 123              
# attempt = 1
# while attempt <=3:
#     u = input("enter your username")
#     p = input("enter your password")

#     if u == username and p == password:
#         print("login successful")
#         break
#     elif u!= username and p != password:
#         print("invalid username or password")
#         attempt +=1
# if attempt > 3:
#     print("account locked due to many attempt")






# 5. Find the second largest of three numbers.


# 6. ATM withdrawal system.

# withdrawal = int(input("enter the number your want to credit: "))
# if withdrawal <=1000:
#     print("your balance amount is successfully out")
# else:
#     print("insufficient balance")


# 8. Restaurant bill with discount.
# discount = int(input("discount allocated: "))
# if discount >=5000:
#     print("you got the discount")
# else:
#     print("you are not the member of discount client")


# 9.Movie ticket pricing based on age.
# age = float(input("enter your current age: "))
# if age >=0 and age <=12:
#     print("you need to paid 150 per person")
# elif age >=13 and age <=19:
#     print("you need to paid 200 per person")
# elif age >=20 and age <=59:
#     print("you need to paid 400 per person")
# elif age <=60 and age <=100:
#     print("you need to paid 100 for special senior citizen")
# else:
#     print("invalid number")

#11. OTP VALID SYSTEM.

# OTP = "1234567"              
# attempt = 1
# while attempt <=5:
#     OTP_Token = input("enter your number")

#     if OTP == OTP_Token:
#         print("login successful")
#         new_password = input("Enter your New Password:")
#         confirm_password = input("confirm password:")

#         if new_password == confirm_password:
#             print("Password Changed Successfully")
#         else:
#             print("Invalid Passoword")
#         break
#     elif OTP != OTP_Token:
#         print("invalid OTP TOKEN")
#         attempt +=1
# if attempt > 3:
#     print(" TRY AFTER 5 MIN due to invalid attemps: ")


opt = "123!@#"
attempt = 1
while attempt <=5:
    opt_token = input("enter the number: ")

    if opt == opt_token:
        print("login successfully")
        new_password = input("enter the password")
        confirm_password = input("enter the password")

        if new_password == confirm_password:
            print("new password is set successfully:")
        else:
            print("invalid username or password")
        break
    elif opt != opt_token:
        print("invalid password")
        attempt +=1

if attempt >5:

    print("try after 3 min")




#======================= Calculator==========================


# u1= float(input("enter any number:    "))
# u2 = float(input("enter any number:   "))
# op = input("enter your operator sign(+,-,*,/):      ")

# if op == "+":
#     print("the addition of your number is: ", u1 + u2)

# elif op == "-":
#       print("the substraction of your number is: ", u1 - u2)
# elif op == "*":
#       print("the multiplication of your number is: ", u1 * u2)
# elif op == "/":
#     if u2 !=0:
#       print("the division of your number is: ", u1 / u2)

#     else: 
#         print("your number is not division:  ")

# else:
#     print("you put the wrong opetator:  ")

u1= float(input("enter any number:    "))
u2 = float(input("enter any number:   "))
op = input("enter your operator sign(+,-,*,/):      ")

if op=="+":
    print("your addition is :" , u1 + u2)


if op=="-":
    print("your sub is :" , u1 - u2)

if op=="+":
    print("your multiplication is :" , u1 * u2)

if op=="/":
    if u2!=0:
        print("it is not division")
        
    print("your division is :", u1 / u2)
    
else:
    print("invalid")
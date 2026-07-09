# # Operators :
# # operators is a symbol that performs certain operation between operands.
# #  for example
# #  c = a + b
# #  here,

# # =,+ are operators. 
# # a,b,c are operands

# # # types of operatoors:
# # 1. arithmetic operators:  we can use operator to perfom logical and mathematical calculations.
# #                      a. + (addition operator)
# #                     b. - (subtraction operator)
# #                     c. * (multiplication operator)
# #                     d. / (division operatior)
# #                     e. % (modulus operator)
# #                     f. ** (power operator or exponential operatior)
# #                     g. // (floor division operatior)


# #example
# ##################################################### a. + (addition operator)########################
# # addition operators adds the two or more than two operands
# a = 5   # (=) this is a assign operators
# b = 6

# sum = a + b
# print(sum)     #11


# name = "ram"
# age = "24"
# add = name + age
# print(add)       #ram24  #concatenation property

# ########################################################b. - (subtraction operator)################
# # substration operator sub the two or more than two operands

# a = 5   
# b = 6
# sub = b-a
# sub1 = a-b
# print(sub)   #1
# print(sub1)   #-1

# #############################    c. * (multiplication operator)###################
# # multiplication operation muultiply the two or more than two operands

# a = 5   
# b = 6
# mul = a*b
# print(mul)   #30

# ############################    d. / (division operatior)###############
# # division operation divide between the  two operands

# num1 = 30
# num2 = 5
# div = num1/num2
# print(div)  #6.0

#    ######### e. % (modulus operator)#################
# # it gives the reminder after division 
# num1 = 30
# num2 = 5
# mod = num1%num2
# print(mod)      #output : reminder



# ###############  F (** ) (power operator or exponential operatior)###############
# # it calculate thepower of interger value
# a = 5  
# k = a**5
# print(k)  #3125



# ########################  g (//) (floor division operatior)######################
# # it only give the whole 
# a = 3.14
# b= 1.5 
# result = a//b
# print(result)       #output :2.0        #process is divide but remove after the (.)




# #radius of circle is 15m then finds it area. formula = pir*r**2
# radius = 15
# area = 3.14*radius**2
# print(area)
# # W.A.P  to take length and width from user and find the area and perimeter of rectangle output: the area of recanagle is :
# a = float(input("enter the value of length: "))
# b = float(input("enter the value of breath: "))
# area = a*b
# perimeter = 2 (a+b)
# print( "the area of rectangle is:" , area)
# print( "the area of rectangle is:" , perimeter)



# +===================================================
"""
        Operators:
            # Operators is a symbol that performs certain operations between operands.
            for example:
            c = a + b

            #Here,
            =,+  are operators.
            a,b,c are operands.

            #Types of Operatiors:
            1. Arithmetic Operators: 
                    a. + (addition operator)
                    b. - (subtraction operator)
                    c. * (multiplication operator)
                    d. / (division operatior)
                    e. % (modulus operator)
                    f. ** (power operator or exponential operatior)
                    g. // (floor division operatior)

                    
            2. comparasion operator(Relational operatior):
                    #Used to compare two values.
                    #Return True or False.
                a. == (equal to operator)
                b. != (not equal to )
                c. >  (greater than)
                d. >= (greater than or equal to)
                e. < (less than)
                f. <= (less than or equal to)

                

        3. Assignment Operator:
                a. = (assignment operator)
                b. +=(addition assignment operator)
                c. -=
                d. *=
                e. /=
                f. %=
                g. **=
                h. //=


        4. Logical Operatior:
                a. or
                b. and 
                c. not


        5. Membership Operator:
                #membership operator is used to check value exists(present) in the sequence(eg:string,list,tuple,etc.) or not.
                #Returns True if value exist(present) otherwise return False.
                a. in
                b. not in
        
                
        6. Identity Operator:
                #Checks the memory location of two objects(variable).
                #Return True or False.

                a. is:
                        #Returns True if both object(variable) have same memory location, otherwise return False.

                b. is not:
                        #Return True if both object(variable) have not same memory location, otherwise return False.

                        

        7. Bitwise operator:            works on bit.
                a. | (Bitwise or operator)
                b. & (Bitwise and operator)
                c. ~ (Bitwise not operator)    #Shitt + TapKoMathikoButton
"""

#1. Arithmetic Operator: [+, -, *, /, %, **, //]
# a = 5
# b = 2

# print(a+b)        #7
# print(5+2)

# print(a-b)          #3
# print(a*b)          #10
# print(a/b)          #2.5
# print(a%b)            #1                   #gives remainder
# print(11%3)         #2

# print(a**b)           #25
# print(2**5)             #32

# print(a//b)             #2




#2. Comparison Operator(Relational Operator):  [==, !=, >, >=, <, <=]
#Return True or False

# a = 5
# b = 3

# print(a == b)  #False
# print(a != b)    #True
# print(a>b)      #True
# print(a>=b)     #True
# print(a<b)          #False
# print(a<=b)         #False


#3. Assignment opertors: [=, +=, -=, *=, /=, %=, **=, //=]
# a = 5
# b = 2

# a+=b            #a = a+b
# a-=b             #a = a-b
# a+=5            #a = a+5 
# a*=b            #a = a*b
# a/=b            #a = a/b
# a**=b           # a = a**b   
# a%=b               # a = a%b     # answer is a reminder, when division is conducted.

# a//=b             #a = a//b              

# print(a)






#4. Logical operatiors: or, and, not
        #Works on boolean values.[i.e. Return True or False]


# print(True or True)             #True

# print(5>2 or 3<1)                # print(True or False)            #True

# print(True or False)            #True
# print(False or False)           #False
# print(False or True)               #True

# # print(True and True)            #True
# # print(True and False)           #False
# print(False and True )
# print(False and False)


# print(5>2 and 3<1)              #print(True and False)  #False




#5. Membership Operators:  

# print("d" in "deepak")        #True
# print("dk" in "deepak")         #False
# print("wx" in "deepak")         #False


# print("d" not in "deepak")        #False
# print("dp" not in "deepak")        #True
# print("wx" not in "deepak")         #True


# name = "deepak"

# print("d" in name)              #True



#6. Identity Operators: is, is not

# a =[1,2,3]
# b= [10,20,30]
# c = [1,2,3]
# d = a

# print(a == c)         #True             #== operator checks value
# print(a is c)           #False

# print(a is d)       

# print(b is c)           #False
# print(c is d)           #False


# print(a is not c)       #True
# print(c is not d)       #True

# print(a is not d)       #False




# x = 10
# y = 20
# z = 10

# print(x == z)   #True           #value check
# print(x is z)   #True           #memory location check




#7. Bitwise Operators: |, & , ~
# print(a&b)              #0
# follow this rule######
# 0 = 0000
# 1 = 0001
# 2 = 0010
# 3 = 0011
# 4 = 0100
# 5 = 0101
# 6 = 0110
# 7 = 0111
# 8 = 1000
# 9 = 1001

# a = 5
# b = 1

# print(a|b)              #7


# print(~(a+b))               #~5         #add 1 and add -ve sign          #-6


# print(~(a|b))           #~7                     #add 1 and add -ve sign #-8



a = 5
b = 4
d = 5
e = a

a is e
print(a)
print(e)
print(a is e)


a = ["a","b","c"]
b = [1,2,3]
c = [4,5,6]
d = a
e = [1,2,3]
print(a is d)
print(a == b)   #only check key
print(b is e) # is consider to check both variable and key 

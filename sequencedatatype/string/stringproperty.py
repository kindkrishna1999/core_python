#
# 
# #############################string property###################


                    #concatination property(+)#################
                    # join the two string
                    # syntax: 
        


# var1+var2           #where we can see there is two variable and it combined or joined to from any two string

#example
# var1="car"
# var2="tesla"
# result=var1+var2
# print(result)           #cartesla
# print("car"," ","tesla")


# var1="krishna"
# var2="kumar"
# result=var1+var2
# print(result)
# print("krishna", " ", "kumar") 

# var1="abcdefg"
# var2="hijklmno"
# result=var1+var2
# print(result)                           #abcdefghijklmno
# print("abcdefg","hijklmno" , sep=" ")    #abcdefg hijklmno only one space will show as result


# num = "1"
# num2 = "2"
# result = num+num2
# print(result)


###########2. id############ : it gives the memory address where the data (value is located).
# name="saroj"
# rollno = "5"
# weight = "50"
# cla= "5"
# print(id(name))          #2041286770800
# print(id(rollno))       #2041285208048
# print(id(weight))       #2041286771056
# print(id(cla))          #2041285208048
# k="my name is krishna kumar pariyar"
# print(id(k))


                            #indexing : it access teh string character by using index value.
# name="saroj"
# k=name[0]
# print(k)                                    #s
# # rollno = "52222"
# # p=rollno[0]
# # print(p)
# pariyar = "rudrachandradevgangakrishnasunita"
# p=pariyar[0]
# print(p)
# print(len(pariyar))


# num = 1234
# print(num[0])           #TypeError: 'int' object is not subscriptable but if you put in string then it is accessable

# print(num[5])  #error



                        #############4 len()#####
# name = "krishna"
# print(len(name))
# k = "enclopeydia"
# print(len(k))


                         #6. slicing():
##  process of accessing the parts (portions ) of swquence data type (stirng, list, tuple, etc.)
#syntax:
# variable Name[start_index:end_index:step]
# NotADirectoryErrorend_index value is not included.
# by deafualy, step=1



############+ve########
# name ="saroj"
# text=name[0:3]
# print(text)
# print(name[0:3:])


# address= "bhaktapurklxfvalkjakj"
# print(address[0::4])                #btrfkj
# print(address[3:6])                 #kta
# print(address[-2:2])    

# book="encyclopedia" #, "ncy" , "ope" , "ncyclop"
# print(book[0:4])
# print(book[6:9])
# print(book[1:8])

###########-ve############

# name ="saroj"
# print(name[-3:-1])
# address="Bhaktapur"
# print(address[-5:-4])
# print(name[-8:-4])


# book="encyclopedia"             #, "ncy" , "ope" , "ncyclop"
# print(book[-11:-8])
# print(book[-6:-3])
# print(book[-11:-4])



# name = input("words of the days: encyclopediaencyclopedia ")
# print(name[2:6])        #cycl
# print(name[-5:-1])      #pedi
# print(name[0::3])       #eyodeyod




#1.Write a program to take a string from the user and print the first character, second character, and last character using indexing.


# name = input("enter your name: ")
# print(name[0:4])



#2.Write a program to take a string from the user and print the first 4 characters and last 4 characters using slicing.


# n = input("enter your letter: ")
# print(n[0:4])
# print(n[-1:-4])

#3.Write a program to take a string from the user and print the string in reverse order using negative slicing.

# name = input("character: ")
# print(name[-1:-5])

# #4.Write a program to take a string from the user and print every second character from the string.

# name = input("character: ")
# print(name[0::2])
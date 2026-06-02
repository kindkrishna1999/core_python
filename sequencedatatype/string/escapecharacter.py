# escape character in python is the special type of character whaich have their won special funciton.



#   1. \n.................
# it breaks the line and switch to next. it only work for string. which mean \n should be in the form of "\n"
# example
# print("college \nname")
# print(5,"\n",3,sep="")         
# # sep="" it reomcies extra space.      backslash n switch to next line (output)
# # output:print in one line vertically
# print(5,4,3,sep="+")

# 2. carriage return...............(\r)
# carriage return : it moves the cursor to the beginning fo the same line without moving to the next line.

# print("hel\ro")  # oel
# print("stud\rent")  #entd  \
# e replaces s
# n replaces t
# t replaces u
# d remains at the end because it was not overwritten

# Final result:
# print("college\rname")
# print("acb\r123")
# print("krishna\rkumar")



# print("12589\rram")   #ram89
# print("sajha\rtech")   #techa
# print("lap\rtop")        #top
# print("univer\rsity")   #sityer

# 3..................\t
#it provides four space in single line. always used string
#example

# print("hel\to")
# print("12589\tram")   
# print("sajha\ttech")   
# print("lap\ttop")        
# print("univer\tsity")

# 4.......................\v
# verticle space
print("he\vllo")
# print("12589\vram")   
# print("sajha\vtech")   
# print("lap\vtop")        
# print("univer\vsity")

#5.......................\b
print("he\bllo")
print("12589\bram")   
# print("sajha\btech")   
# print("lap\btop")        
# print("univer\bsity")

# print("univer\b")
# print ("he\bllo")
# print("hexxx1\blo")

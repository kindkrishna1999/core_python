############################ 1. concatination property(+) : it joins the two lists
# lst1 = [10,50,60]
# lst2= ["saroj","ravi","krishna"]
# v = lst1+lst2
# print(v)                        #output:     [10, 50, 60, 'saroj', 'ravi', 'krishna']
# a=[5,5,5,5]
# b=[5,5,5,5,5]
# v=a+b
# print(v)                    #[5, 5, 5, 5, 5, 5, 5, 5, 5]


# ############################ 2. indexing ####################: it access the list elements by sing index number.
# lst1 = [10,50,60,50,90,11,54,68,44]
# v=lst1[2]
# print(v)                #60

# lst1 = [10,50,60,50,90,11,54,68,44,5,5,5,5,5,5,5]
# v=lst1[1::4]
# print(v)                #[60, 54]


########################## 3 slicing########################
# process of accessing the parts (portions ) of sequence data type (string, list, tuple, etc.)
#syntax:
# variable Name[start_index:end_index:step]
# NotADirectoryErrorend_index value is not included.
# by deafualy, step=1


# lst1 = [10,50,60,"saroj","55.5"]
# print(lst1[1:4])            #[50, 60, 'saroj']


#question 
# lst1 = [10,50,60,"saroj","55.5"]
# print(lst1[-3:])   show all because of end is not fix

############################## nested list:#########################it define as list inside list
lst1 = [10,50,60,"saroj","55.5"]
lst2 = ["a","b"]
v = lst1+[lst2]
print(v)
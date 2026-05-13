#for changing in tuple, we have to convert tuple into list temporarily
#then change into the list and then convert list back to tuple

contries = ("Spain","Italy","India","England","France") #tuple created

temp = list(contries) #temporary variable that holds the converted tuple into list
temp.append("Russia")   #add item (methods of list will be used)
temp.pop(3)     #delete item--India will be deleted by method "pop"
temp[2] = "Finland"  #change/replace item
contries = tuple(temp)  #change the temporary list back to tuple
print(contries) #prints new tuple

tup = (0,1,2,3,2,30,1,3,2,4,3)

count = tup.count(1)
print("Number of 1 in tuple is ", count)
index = tup.index(4)
print("Index of 4 in first occurance is :",index)
co = tup.index(3,4,8) #finds index of 3 from range 4 to 8
print("Index of first occurance of 3 from range 4 to 8 is : ",co)

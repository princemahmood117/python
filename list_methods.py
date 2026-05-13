l = [1,6,2,19,1,7,3,15]
print("Given list is : ",l)
l.append(8) #method to add an item given inside the bracket into the list
print("Appended values to the last is : ",l)

l.sort()    #method to sort items as ascending
print("Sorted in ascending order is : ",l)

# l.sort(reverse=True)  #method to sort items as descending
# print(l)

l.reverse()
print("Reversed List L is : ",l)

# print(l.index(19))   #finds the index of the value given inside the bracket

# print(l.count(1)) #counts how many occurances the given value inside the bracket

# m = l.copy()  #method to copy items from one list to another list
# print(m)

l.insert(3,899) #l.insert(index_number,new_value) inserts new value into defined index number
print("Inserted list is :",l)

m = [100,200,300,400]
l.extend(m)   #method to open_up list M and put it on the last of list L
print("Entended list is : ",l)

k = l+m    #can concate two list and make a new list
print("New list after ooncatenation:",k)

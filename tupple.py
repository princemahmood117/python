# tup = (1,3,5)
# print(type(tup),tup) #class type "tupple"

# tup = (1) #single value will show the type is int, have to add an comma after value
# tup = (1,) #example,comma will make itself has another value to be a tupple
# print(type(tup))

#tupples are unchangeable

tup = (1,2,76,342,32,"Green",True)
print("Length is : ",len(tup))
print(tup[0])
print(tup[-1])

if 342 in tup:
    print("Number Is Present")
else:
    print("Number Not Present")

tup2 = tup[1:4]  #slicing can be done here too
print(tup2)

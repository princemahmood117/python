marks = [3,5,6,"Prince",4, 8,10,11,2]
# print(marks)
# print(type(marks))
# for i in marks:
#     print(i)

#Negative Indexing

# print((marks[-3]))  #negative index
# print('\n')
# print(marks[len(marks) - 3])  #positive indexing--->length = 5
# print(marks[5-3])
# print(marks[2])
# print(marks[1])

#If an item is present on the list or not

# if "Prince" in marks:
#     print("Yes")
#
# else:
#     print("NO")

# if "ine" in "Prince":
#     print("YES")
# else:
#     print("NO")

# print(marks[4])
# print(marks)
# # print(marks[1:4])
# print(marks[0:9:2])  #Jump in list, here it jubped by 2

#Jump in list

# animals = ["cat", "doggo", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[0:9])
# print(animals[1:8:3])
# print(animals[0:8:3])

#List_Comprehesion

lst = [i*i for i in range(4)]
print(lst)
print('\n')


lst1 = [i for i in range(10) if i%2 == 0] #from 0 to 9 divided by 2 and remaing 0 will be printed
lst2 = [i*i for i in range(10) if i%2 == 0]

print(lst1)
print(lst2)
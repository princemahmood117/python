ep1 = {
    122 : 45,
    123 : 89,
    567 : 69
}

ep2 = {
    222 : 67,
    566 : 90
}

ep3 = {
    100 : 50,
    200 : 55,
    300 : 60
}

ep4 = {
    400 : 50,
    500 : 55,
    600 : 60
}

ep5 = {
    700 : 50,
    800 : 55,
    900 : 60
}

#UPDATE
ep1.update(ep2)    #adds all "values and keys" of ep1 to ep and updates it
print("After updating", ep1)

print()

for i in ep1.keys():
    print("Keys", i)

print()

for j in ep1.values():
    print("Values",j)
print()

#clear()--->clears all inside a dictonary, output : {}
ep3.clear()
print("after clear ", ep3)

#pops(removes and item given inside the first bracket)
print(ep4)
ep4.pop(400)
print("After clearing specific item ", ep4)

#popitem()--->removes the last key-values from dictoonary
ep4.popitem()
print("After removing last item using popitem() ", ep4)

#del dict_name ----> deletes the dictonary ep5 and after printing it will show error
print(ep5)
del ep5[800]  #here the specificly key 800 with it's value will be deleted
print(ep5) #if not specified, the entire dictonary will be deleted

print()

ep6 = {
    1000 : 70,
    2000 : 80,
    3000 : 90
}

for a,b in ep6.items():  #keys will go to - a, values will go to - b
    print(a,b) 
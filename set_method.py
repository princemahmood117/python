s1 = {1,2,5,6}
s2 = {3,6,7}
print("Union is ", s1.union(s2) )
print("Intersection is ", s1.intersection(s2))

print("")

cities1 = {"tokyo", "madrid","Berlin"}
cities2 = {"tokyo", "seoul", "kabul"}

cities3 = cities1.union(cities2) #union using variable
print(cities3)

cities1.intersection_update(cities2)
print(cities1) #the value common between 2 sets will be the new value of cities1

print("")

cities4 = {"tokyo", "madrid","Berlin"}
cities5 = {"tokyo", "seoul", "kabul"}

cities6 = cities4.symmetric_difference(cities5)
print(cities6) #intersection values will be deleted in new set

cities7 = {"tokyo", "madrid","Berlin"}
cities8 = {"tokyo", "seoul", "kabul"}

cities9 = cities7.difference(cities8)
print("Cities_9 is", cities9) #prints those in 7 but not in 8 (technically A-B)



#DISJOINT = NOT INTERSECT ITEMS
a = {9,10,20,15}
b= {10,11,17,20}
c = {13,18,27,60}
d = {100,150,111,121}

e = a.isdisjoint(b)
f = c.isdisjoint(d)

print(e) #prints False if items in A are present in B also
print(f) #prints True if items in C are not present in D also



#SUPERSET = if all items present in b are present in a, then prints TRUE

A = {10,11,12,13}
B = {14,15,16,17} #ALL items of B is not part of A, so false
C = {18,19,20,21}
D = {21,20,18,19} #ALL items of D are present in C
print("About Superset : ", A.issuperset(B))  #false
print("About Superset2 : ", C.issuperset(D)) #true

#SUBSET = D is subset of C ----> prints True
print("About Subset : ", D.issubset(C))



#ADD any SINGLE item to a set

p = {10,11,12,13}
p.add(14)
print("After adding new item : ", p)

#ADD MULTIPLE items to a set

q = {20,21,22,23}
r = {25,26,27} #have to create another list/tuple/set and use update formula
q.update(r)
print("After adding multiple items : ", q)



#REMOVE : Rises an error after not finding the item you want to delete
#DISCARD : DOESN'T Rise an error after not finding the item you want to delete

g = {10,11,12}
# g.remove(15)
# print(g)   #remove comment to see the result,doens't execute next lines

g.discard(15)
print(g)



#pop() ----> removes an random item from the list (we dont know which)

item = {10,11,13}
x = item.pop()
print(x)

item.clear()    #clears items inside the set
print("About clear : ", item)



#check if item exists

info = {10,11,12,13}
if 10 in info:
    print("Value is present")
else:
    print("Value not present")

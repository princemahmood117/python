#dictonaries are ordered collection of data items
#stores multiple items in a single variable

dic = {
    1 : "Harry",      # key : key_value
    5 : "Prince",
    10 : "Navid",
    15 : "Siam"
}

print(dic)  #prints all

print("")
#particularly prints values inside dictionary
print(dic[1])
print(dic[5])
print(dic[10])
print(dic[15])

print(dic.get(2))  #get method will be used by first bracket,keys inside it
#get method will throw NONE if there is an error

print(dic.keys())    #prints all the keys used in dictonary
print(dic.values())  #prints all the values used in dictonary

#using loop
for key in dic.keys():
    print(key)
print("")
for i in dic.values():
    print(i)


print(dic.items())
for key, value in dic.items():
    print(f"Corresponding value for the key {key} is {value}")
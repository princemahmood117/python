string = " this"
print(string.strip())  # removes the first spaces from the string

string2 = " this is a string with space"
print(string2)
print(string2.strip())


leftStrip = " this removes the left side space"
print(leftStrip)
print(leftStrip.lstrip())


rightStrip = "this removes the right side space "
print(rightStrip)
print(rightStrip.rstrip())


endswith = "this text ends with one"
print(endswith.endswith("one"))  #returns true or false



print(",".join(["this", "is", "Joined", "by", "comma"]))
print("...".join(["this", "is", "Joined", "by", "dot"]))

print('\n-------- Spilit methos ---------\n')

print("this is a splited sentence".split())  # splited by comma inside []


anotherSplit = "This is python language"
storedSplit = anotherSplit.split()
print("Stored Splited " + str(storedSplit))  
print("First element is : " + storedSplit[0])


# print(split[1])

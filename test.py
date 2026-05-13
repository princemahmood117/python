a = "Harry!!!!"
print(len(a))
print(a.upper())

print(a.rstrip("!"))  #removes unwanted marks

print(a.replace("Harry","john")) #replaces one by another

str1 = "Welcome to the console!!!"
print(len(str1))

print(len(str1.center(50)))

print(str1.count("o"))   #count anything

print(str1.endswith("!!"))  #tells if the string ends with specific character or not

str2 = "He is a good man who is a  student"
print(str2.find("is"))  #shows the index of first occurance of seraching sub-string


str3 = "Go with the flow"
print(str3.startswith("Go")) #tells if the string starts with specific character or not

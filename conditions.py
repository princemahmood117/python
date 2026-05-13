# greater than ">"
# less than "<"
# greater than ">="
# less than or equal "<="
# not equal to "!="
# if - else - elif

a = int(input("Enter your age : "))
print("Your age is :", a)

print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a!=18)

if (a>18):
    print("You can enter")

else:
    print("You can't enter")

price = 210
budget = 200

if(price < budget):
    print("Pack One kilo of apple")
else:
    print("Leave it, I am poor")


num = int(input("Enter a number : "))
if(num < 0):
    print("Number", num,  "is negative")
elif(num == 0):
    print("Number", num, "is Zero")
else:
    print("Number", num, "is positive")
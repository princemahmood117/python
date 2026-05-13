

num = int(input("Enter any number : "))

if(num < 0):
    print("Number is negative")
elif(num > 0):
    print("Number is positive")

    if (num > 0 and num <= 10):
        print("Number is between 0 to 10")

    elif (num > 10 and num <= 20):
        print("Number is between 11 to 20")
    elif (num > 20 and num <= 30):
        print("Number is between 21 to 30")
    elif (num > 30 and num <= 40):
        print("Number is between 31 to 40")

else:
    print("Number is zero")
print("Code ran successfully")
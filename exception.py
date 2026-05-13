# error ends the execution of any program
# by exception-handling we can skip the error part and execute the rest

a = input("Enter the number : ")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")

except:
    print("Invalid input")

print("Some codes here")
print("Here it ends")


# WE can also handle a specific type of exception or error

# int() ----> specifies that the value entered must me integer only

# if not entered integer, it will rise "ValueError"

#we will handle "ValueError" specifically
try:
    num = int(input("Enter an integer : "))
    print("Entered Integer is : ", num)
except ValueError:
    print("Number is not Integer.")

# we can use multiple "except"


try:
    a = int(input("Enter a number : "))
    x = [6,10]
    print(f"Value at index {a} is : ", x[a])
except ValueError:
    print("Number not integer.")
except IndexError:
    print("Index error here")
finally:
    print("It is finally and it will must be executed ")

# there is a keyword "finally"
# which is used for execute the lines even it goes or not inside the try / except

# "finally" is very useful inside function


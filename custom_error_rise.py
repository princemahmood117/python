#custom error rise by the user

# a = int(input("Enter any value between 5 and 9 : "))
# if (a < 5 or a > 9):
#    # raise ValueError("Value should be between 5 and 9 ") #prints this line in error
#  print(a)

# rise and error if value entered not between 5 to 9
# type 'quit' to exit the code
user = input("Enter Value : ")
if user.lower() == 'quit':
    print("Exiting the code")
else:
    try:
        a = int(user)
        if (a < 5 or a > 9 ):
            raise ValueError("Value must be between 5 and 9 or type 'quit' to exit")
        elif(a == 5 or a < 9):
            print("Value ", a, " is corect")
        else:
            raise ValueError("Value must be between 5 and 9 or type 'quit' to exit")
    finally:
        print("Bye Bye")


    # except ValueError:
    #     print("Value must be between 5 and 9 or type 'quit' to exit")
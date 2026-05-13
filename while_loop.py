#in while loop, we have to initialize a number first

# i = 0
# while (i<3):
#     print(i)
#     i = i + 1  #increment in loop

# i = int(input("Enter the number : ")) #takes a number
# if(i>0):
#     print("Number is positive") #checks if number is positive
#     while(i<50):
#         print(i)    #prints input value and increments by 1
#         i = i + 1
# else:
#     print("Number is not postive") #if number not positive,direct executes this line
# print("Number Printed")

# i = 5
# while (i>0):
#     print(i)
#     i = i  -  1  #decrement in loop
#
# else:       #else can be used in while loop, if the condition is false
#     print("Condition checking false")

#for false conditon

# i = -5
# while(i>0):
#     print(i)
#     i = i - 1
# else:
#     print("Condition is false")

# there is no do_while loop in python because
# do_while loop always executes the loop body
# at-least once weither the condition is true or false
# and then will check the condition for next one to execute

#for using do_while in python we use "while True" as infinite loop

# i = 0
# while True:
#     print(i)
#     i = i+1
#     if(i%100 == 0): #after finding the condition the loop will exit
#         break


while True:
    number = int(input("Enter a positive number : "))
    print(number)
    #takes input and print until finds a negative,if neagtive the loop will exit
    if not number > 0: #not means inverse of that number
        break
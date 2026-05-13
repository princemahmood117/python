#break statement helps to skip a part of code/eixt the loop

# for i in range(12):  #i will take values from 0 to 11
#     print("5 X", i, "=", 5*i )  #will print until i = 11
#
#     if(i == 10): #loop will exit after finding the value iof i = 10
#         break


#continue statement means skip the iteration

for i in range(12):
    if(i%2 == 0):
        print("Iteration skipped")
        continue   #this iteration will not be printed, means it will be skipped
    print("5 X", i, "=", 5*i)


#using break in while loop

while True:
    number = int(input("Enter a positive number : "))
    print(number)
    #takes input and print until finds a negative,if neagtive the loop will exit
    if not number > 0: #not means inverse of that number
        break
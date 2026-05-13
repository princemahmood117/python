

x = int(input("Enter the value of x : "))

match x:                   #cases will match the values of x if true
    case 0:
        print("x is zero") #case is what we want to check if true
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case 3:
        print("x is three")
    case 4:
        print("x is four")

    case _ if x!=4:                            #for default case(if false)
        print(x, "is not between zero to four")
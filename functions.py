# print("Before using Function")
# a = 9
# b = 8
# gmean1 = (a*b) / (a+b)
# print(gmean1)
#
# c = 7
# d = 6
# gmean2 = (c*d) / (c+d)
# print(gmean2)
#here we used same formula twice(multiple times which is time consuming
#let us do this by using FUNCTION
# print('\n')


print("Using Function")
def CalculateGmean(a,b):  #function defined with function_name & arguments into it
    mean = (a*b) / (a+b)
    print(mean)

def isGreater(a,b):  #def function_name(arguments):
    if(a>b):
        print("First Number is Greater")
    else:
        print("Second Number is Greater")

def isLesser(a,b):
    pass  #pass means i will write the function body letter, it wont generate error

a = 9
b = 8
isGreater(a,b)
CalculateGmean(a,b)

c = 7
d = 67
isGreater(c,d)
CalculateGmean(c,d)


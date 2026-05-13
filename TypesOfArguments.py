#(1)Default Arguments
def average(a=9,b=1):  #Default arguments
    print("The Average is " , (a+b)/2)
# average() #this will be used if only default arguments are set
average(1,5) #these values will replace the default values
#if we only pass one value into argument, the value will replace only 'a'

def name(fname,mname="Mahmood",lname="Prince"):
    print("Hello",fname,mname,lname)

name("Iftekhar") #only fname got the value changed because it wasn't defined before

#(2)Keyword Arguments---we do not need to follow orders of arguments

def avg(a = 3, b = 4):
    print("The Average is : ", (a+b)/2)
# avg()
avg(b=2,a=1) #a & b not in order but interpreter will execute correctly if keywords are set


#(3)Required Argument---Must give one argument

def sum(a,b,c=1):
    print("The Sum is : ",  a+b+c)
sum(a=5, b=6) #a&b are set here and c is taken by default


#(4)Variable-Length Argument----

def avrg(*numbers):
    # print(type(numbers)) # it is a tupple
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The Avgerage is : ", sum/len(numbers))

avrg(5,6) #as many numbers will be counted as the length, here it is 2

#Return Statetment

def avrg(*numbers):

    sum = 0
    for i in numbers:
        sum = sum + i
        # return 7
    return sum / len(numbers) #returns values to the calling function
c = avrg(5,6,1)  #here avrg(5,6,1) is calling function
#if 2 return used, first one is used in execution
print("The Avrg is ", c)



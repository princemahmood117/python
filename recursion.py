#factorial(7) = 7*6*5*4*3*2*1 {(6*5*4*3*2*1) == factorial(6) or factorial(7-1)}
# factorial(n) = n * factorial(n-1)
# factorial(7) = 7 * factorial(7-1)
# factorial(7) = 6 * factorial(6-1)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1) #formula for factorial
#
# print(factorial(5))
# print(factorial(6))
# print(factorial(7))
# print(factorial(8))
# print(factorial(0))
# print(factorial(1))

#FIBONACCHI_SERIES
#f(n) = f(n-1) + f(n-2)
def fibo(n):
    if(n<0):
        print("Incorrect number")
    elif (n == 0):
        return 0
    elif(n == 1) or (n == 2):
        return 1
    else:
         return (fibo(n-1) + fibo(n-2))

print(fibo(6))
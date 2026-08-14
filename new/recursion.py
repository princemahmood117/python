def countdown(n):
    # 1. Base Case: Stop when n hits 0
    if n <= 0:
        print("Blast off!")
        return
    
    # 2. Print current number
    print(n)
    
    # 3. Recursive Step: Call the function again with a smaller number (n - 1)
    countdown(n - 1)

countdown(3)


def factorial(n) : 
    if n < 2 : 
        return 1
    return n * factorial(n -1)
n = 5
print(f"factorial of {n} is {factorial(n)}")


#return sum of all positive numbers

def sumPositive(n) :
    if n < 1 : 
        return 0

    return n + sumPositive(n - 1)

print(sumPositive(3))


def fact(n) :
    if n < 2: 
        return 1

    return n * fact(n - 1)

print(fact(1000))
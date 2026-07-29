#1
y = 0

while y < 20 :
    print("this is the current value of y = " + str(y))
    y = y + 1


#2
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x = x + 1
    print("Done")

attempts(5)        


#3
x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

print(sum)    


product = 1
while x < 10:
    product = product * x
    x = x + 1

print(product)



#4

if(x != 0) :
    while(x % 2 == 0) : 
        x = x / 2

#5
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n = n + 1

print_range(1, 5)






#6
def is_power_of_two(number):

    if number == 0 :
        return False
    else :
        while number % 2 == 0:
            number = number / 2

    if number == 1:
        return True
    return False


print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
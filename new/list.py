x = ["Now", "we", "are", "cooking!"]   # this is list
print(type(x))

for ar in x:
    print(ar)


y = {"Now", "we", "are", "cooking!"}   # this is set
print(type(y))


x = ["Lion", "Zebra", "Monkey", "Tiger"]

char = 0

for animal in x:
    print(animal, " - ", len(animal))
    char = char + len(animal)

print("Total characters:", str(char))
print("Average characters: {}".format(char / len(x)))


people = ["Donal", "Harry", "Margarate", "Ashly"]

for index, p in enumerate(people):
    print("Index {} is person {}".format(index,p))




def fullEmail(people):
    result = []
    for name, email in people:
        result.append("{} <{}>".format(name, email))
    return result    

personFullName = fullEmail([("Iftekhar", "iftekhar20300@gmail.com")])
print(personFullName)


def skip_elements(elements):
    result = []
    # index tracks the position (0, 1, 2...), element tracks the value
    for index, element in enumerate(elements):
        # Check if the position index is even
        if index % 2 == 0:
            result.append(element)
    return result

# Test cases
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) 
# Output: ['a', 'c', 'e', 'g']

print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) 
# Output: ['Orange', 'Strawberry', 'Peach']


multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)


# List comprehension

mul = [x * 7 for x in range(1,11)]
print(mul)

divi = [x for x in range(1,101) if x % 3 == 0]
print(divi) 


def odd_numbers(n):
	return [x for x in range(1, n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []..............
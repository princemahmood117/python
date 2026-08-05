price = 7.5

with_tax = price * 1.09

print(with_tax)

print("Base price : {:.2f} and with tax price : {:.2f}".format(price, with_tax))


def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.1f} km".format(miles, km )
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
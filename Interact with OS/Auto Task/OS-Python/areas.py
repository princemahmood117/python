#!/usr/bin/env python3

import math

def triangle(base, height):
	return base/height*2

def rectangle(base, height):
	return base*height

def circle(radius):
	return math.pi*(radius**2)


result1 = triangle(5, 10)
result2 = rectangle(5, 10)
result3 = circle(5)

print("area of triangle is " + str(result1))
print("area of rectangle is " + str(result2))
print("area of circle is " + str(result3))

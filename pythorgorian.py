import math
from math import sqrt
print ("The Pythagorian Theorem calculates the Hypotenuse of a triangle")
def Pythagoras(a,b):
    theorem = ((a**2) + (b**2))
    return theorem
a = float(input("Please input a number for A squared "))
b = float(input("Please input a number for B squared "))
content = Pythagoras(a,b)
content = sqrt(content)
print ( "The Hypotenuse is  ", content)

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

def Pythagorian (p,c):
    theory = (sqrt((c * c) - (p * p)))
    return theory
c = float(input("please input the length of side C "))
p = float(input("Please input the length of side A "))
contents = Pythagorian(p,c)
print ("Side B is equal to ", contents)

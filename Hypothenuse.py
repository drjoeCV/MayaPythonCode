import math

def remainingside(a,b):
    return math.sqrt( a*a+ math.pow(b,2) )

print("My name is Maya!")

a = input("Enter the length of one of the sides of the triangle: ")
a = float(a)
b = input("Enter the length of the other side of the triangle: ")
b = float(b)

# compute c
c = remainingside(a,b)

print("The length of the remaining side is", c)
math.avg()

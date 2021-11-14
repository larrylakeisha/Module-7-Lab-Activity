# Lakeisha Larry
# November 14, 2021

# Program 1 returns the area of a circle

def findArea(r):
    pi = 3.142
    return pi * (r*r)


num = float(input("Enter the radius:"))
print("Area is %.6f" % findArea(num))

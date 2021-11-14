# Lakeisha Larry
# November 9, 2021

# Program 2 checks if a number is in the range given

num = (1, 10)


def checkrange(num):
    if num in range(1, 10):
        print("Number is in range", str(num))
    else:
        print("Number is out of range")


checkrange(11)

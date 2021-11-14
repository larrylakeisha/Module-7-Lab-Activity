# Lakeisha Larry
# November 9, 2021

# Program 3 multiplies a list of numbers

numList = [5, 2, 7, -1]


def multiplyList(L):
    # multiply each number in the list

    total = 1
    for i in L:
        total *= i
        return total


print(multiplyList(numList))

# return the value

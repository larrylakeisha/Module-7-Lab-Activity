# Lakeisha Larry
# November 14, 2021

# Program 5 creates image of a box

import turtle


def drawSquare():
    for i in range(4):
        turtle.forward(i)
        turtle.left(90)


wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

drawSquare()

wn.exitonclick()

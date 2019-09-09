import turtle
import random

# non library imports
import utils

# global constants
MAX_SQUARES = 250
MAX_LENGTH = 300


def drawSquare(side, t):
    for i in range(4):
        t.fd(side)
        t.rt(90)
    t.seth(random.randint(0, 360))


def main():
    # turtle initializations
    t = turtle.Turtle()
    turtle.colormode(255)
    t.ht()
    t.speed(0)

    # random amount of squares with pretty colors
    randAmount = random.randint(1, MAX_SQUARES)
    for i in range(randAmount):
        nextCoord = utils.randomCoord()
        color = utils.colorPicker()
        t.pencolor(color)
        t.fillcolor(color)
        utils.moveCursor(nextCoord[0], nextCoord[1], t)
        t.begin_fill()
        drawSquare(random.randint(0, MAX_LENGTH), t)
        t.end_fill()
    turtle.done()


if __name__ == "__main__":
    main()

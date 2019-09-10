import random

# non library imports
import utils


def branch(size, t):
    t.forward(size)
    for i in range(3):
        t.left(45)
        t.forward(size)
        t.backward(size)
        t.right(90)
        t.forward(size)
        t.backward(size)
        t.left(45)
        t.forward(size)
    t.backward(size * 4)


def snowflake(size, t):
    for i in range(8):
        branch(size, t)
        t.left(45)


def drawFlakes(numFlakes, size, stroke, t):
    """
    Generates a specified number of snowflakes in random locations
    """
    t.pensize(stroke)
    for i in range(numFlakes):
        nextCoord = utils.randomCoord()
        color = utils.colorPicker()
        t.pencolor(color)
        utils.moveCursor(nextCoord[0], nextCoord[1], t)
        snowflake(size, t)

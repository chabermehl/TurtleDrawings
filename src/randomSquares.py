import random

# non library imports
import utils

# global constants
MAX_LENGTH = 300


def drawSquare(side, t):
    for i in range(4):
        t.forward(side)
        t.right(90)
    t.seth(random.randint(0, 360))


def drawSquares(numSquares, t):
    '''
    Draws a specified number of squares in random orientations with random colors
    '''
    for i in range(numSquares):
        nextCoord = utils.randomCoord()
        color = utils.colorPicker()
        t.pencolor(color)
        t.fillcolor(color)
        utils.moveCursor(nextCoord[0], nextCoord[1], t)
        t.begin_fill()
        drawSquare(random.randint(0, MAX_LENGTH), t)
        t.end_fill()

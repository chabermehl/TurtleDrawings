"""
Utility functions used throughout the src code
"""

import random

# global constants
MAX_CORD = 200
MIN_CORD = -200


def colorPicker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def randomCoord():
    randX = random.randint(MIN_CORD, MAX_CORD)
    randY = random.randint(MIN_CORD, MAX_CORD)
    return randX, randY


def moveCursor(x, y, t):
    t.pu()
    t.goto(x, y)
    t.pd()

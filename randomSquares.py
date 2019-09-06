import turtle
import random

MAX_SQUARES = 250
MAX_LENGTH = 300
MAX_CORD = 200
MIN_CORD = -200


def drawSquare(side, t):
    for i in range(4):
        t.fd(side)
        t.rt(90)
    t.seth(random.randint(0, 360))


def moveCursor(x, y, t):
    t.pu()
    t.goto(x, y)
    t.pd()


def generateRandoms():
    randSide = random.randint(0, MAX_LENGTH)
    randX = random.randint(MIN_CORD, MAX_CORD)
    randY = random.randint(MIN_CORD, MAX_CORD)
    return randSide, randX, randY


def colorPicker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def main():
    # turtle initializations
    t = turtle.Turtle()
    turtle.colormode(255)
    t.ht()
    t.speed(0)

    # random amount of squares with pretty colors
    randAmount = random.randint(1, MAX_SQUARES)
    for i in range(randAmount):
        randoms = generateRandoms()
        color = colorPicker()
        t.pencolor(color)
        t.fillcolor(color)
        moveCursor(randoms[1], randoms[2], t)
        t.begin_fill()
        drawSquare(randoms[0], t)
        t.end_fill()
    turtle.done()


if __name__ == "__main__":
    main()

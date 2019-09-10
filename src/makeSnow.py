import math
import snowflake
import utils

snowflakes = []


def makeSnow(flakes, size, t):
    snowCount = 0
    noFlake = 0
    while(snowCount < flakes):
        nextCoord = utils.randomCoord()
        if(allowFlake(nextCoord, size)):
            noFlake = 0
            snowflakes.append(nextCoord)
            utils.moveCursor(nextCoord[0], nextCoord[1], t)
            t.pencolor(utils.colorPicker())
            snowflake.snowflake(size, t)
            snowCount += 1
            if(snowCount % 3 == 0):
                eraseFlake(snowflakes[0], size, t)
        else:
            noFlake += 1
            if(noFlake > 5):
                eraseFlake(snowflakes[0], size, t)


def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def allowFlake(nextFlake, size):
    for i in range(len(snowflakes)):
        flakeDistance = distance(snowflakes[i], nextFlake)
        if(flakeDistance < (size * 8)):
            return False
    return True


def eraseFlake(flake, size, t):
    utils.moveCursor(flake[0], flake[1], t)
    t.pencolor((255, 255, 255))
    snowflake.snowflake(size, t)
    snowflakes.pop(0)

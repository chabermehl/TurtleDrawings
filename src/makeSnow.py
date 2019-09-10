import snowflake
import utils

snowflakes = []


def makeSnow(t):
    snowCount = 0
    while(snowCount <= 4):
        nextCoord = utils.randomCoord()
        snowflakes.append(nextCoord)
        utils.moveCursor(nextCoord[0], nextCoord[1], t)
        t.pencolor((0, 0, 0))
        snowflake.snowflake(20, t)
        snowCount += 1
        if(snowCount % 3 == 0):
            utils.moveCursor(snowflakes[0][0], snowflakes[0][1], t)
            t.pencolor((255, 255, 255))
            snowflake.snowflake(20, t)
    # print(snowflakes)

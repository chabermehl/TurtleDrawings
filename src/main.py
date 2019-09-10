import argparse
import turtle
import sys

# non library imports
import randomSquares
import snowflake
import makeSnow


def main():
    # turtle initializations
    t = turtle.Turtle()
    turtle.colormode(255)
    turtle.screensize(400, 400)
    t.ht()
    t.speed(0)

    # arg parsing
    parser = argparse.ArgumentParser()

    parser.add_argument("amount", nargs="?", help="Number of chosen shape to generate", type=int)
    parser.add_argument("size", nargs="?", help="Set the size of the shape", type=int)
    parser.add_argument("-s", "--squares", help="Generates random squares", action="store_true")
    parser.add_argument("-l", "--letitsnow", help="Create a snow falling effect", action="store_true")
    parser.add_argument("-f", "--flakes", help="Create random flakes", action="store_true")

    args = parser.parse_args()

    if(args.squares):
        randomSquares.drawSquares(args.amount, args.size, t)
        turtle.done()
    elif(args.letitsnow):
        makeSnow.makeSnow(args.amount, args.size, t)
        turtle.done()
    elif(args.flakes):
        snowflake.drawFlakes(args.amount, args.size, t)
        turtle.done()


if __name__ == "__main__":
    main()

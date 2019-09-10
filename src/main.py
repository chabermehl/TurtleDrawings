import argparse
import turtle
import sys

import randomSquares
import snowflake


def main():
    # turtle initializations
    t = turtle.Turtle()
    turtle.colormode(255)
    t.ht()
    t.speed(0)

    # arg parsing
    parser = argparse.ArgumentParser()

    parser.add_argument("amount", nargs="?", help="Number of chosen shape to generate", type=int)
    parser.add_argument("-s", "--squares", help="Generates random squares in turtle graphics", action="store_true")
    parser.add_argument("--snowflake", help="Generate a snow flake", action="store_true")

    args = parser.parse_args()

    if(args.squares):
        randomSquares.drawSquares(args.amount, t)
        turtle.done()
    elif(args.snowflake):
        snowflake.snowflake(20, t)
        turtle.done()


if __name__ == "__main__":
    main()

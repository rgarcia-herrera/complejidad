import turtle
import argparse

parser = argparse.ArgumentParser(
    description="turtle draw Koch's curve")

parser.add_argument('--n', type=int, default=3)

parser.add_argument('--sides', type=int, default=3,
                    help='number of sides')

# parser.add_argument('--step', type=int, default=5,
#                     help='length of step')

args = parser.parse_args()


def iteran(k, n):
    rangle = 360.0 / n
    langle = 180 - rangle

    if k == 1:
        turtle.forward(min_step)
        turtle.left(langle)

        for i in range(n-2):
            turtle.forward(min_step)
            turtle.right(rangle)

        turtle.forward(min_step)
        turtle.left(langle)
        turtle.forward(min_step)
    else:
        iteran(k - 1, n)
        turtle.left(langle)

        for i in range(n-2):
            iteran(k - 1, n)
            turtle.right(rangle)

        iteran(k - 1, n)
        turtle.left(langle)
        iteran(k - 1, n)


ts = turtle.getscreen()
width = ts.window_width()
height = ts.window_height()

min_step = width / 3 ** args.n

if min_step < 1:
    min_step = 1

turtle.speed(0)
turtle.penup()
turtle.goto((-1 * (width / 2)) + min_step,
            (-1 * (height / 2)) + min_step)
turtle.pendown()
turtle.tracer(False)



iteran(args.n, args.sides)
turtle.exitonclick()

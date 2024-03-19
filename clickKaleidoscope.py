import turtle
import random

t = turtle.Pen()
turtle.bgcolor("black")
colors = ["white", "green", "blue", "pink"]


def draw_kaleidoscope(x, y):
    size = random.randint(20, 50)
    sides = random.randint(3, 10)
    t.pencolor(random.choice(colors))
    t.width(random.randint(1, 4))
    draw_spiral(x, y, size, sides)


def draw_spiral(x, y, size, sides):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for i in range(20):
        t.forward(2 * i)
        t.right(360 / 4)


turtle.onscreenclick(draw_kaleidoscope(0.0, 0.0))
done()
import turtle
import random

t = turtle.Pen()
turtle.bgcolor("black")
t.pencolor("white")
t.width(random.randint(1,4))
size = random.randint(20,50)
sides = random.randint(3,10)
colors = ["blue", "white", "pink", "green", "red"]
for x in range(10):
    t.pencolor(random.choice(colors))
    t.width(random.randint(1,4))
    size = random.randint(20,50)
    sides = random.randint(3,10)
    t.penup()
    t.setpos(random.randint(1,200), random.randint(1,200))
    t.pendown()
    for i in range(size):
        t.forward(i*2)
        t.right(360/sides)
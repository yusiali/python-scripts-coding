import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["white", "green", "red", "blue"]
for j in range(10):
    size = random.randint(20, 50)
    sides = random.randint(3,10)
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0, turtle.window_height()//2)
    t.pencolor(random.choice(colors))
    t.width(random.randint(1,3))
    angle = t.heading()
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for i in range(size):
        t.forward(2*i)
        t.right(360/sides)
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    t.setheading(180-angle)
    for i in range(size):
        t.forward(2*i)
        t.left(360/sides)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    t.setheading(angle-180)
    for i in range(size):
        t.forward(2*i)
        t.left(360/sides)
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    t.setheading(360-angle)
    for i in range(size):
        t.forward(2*i)
        t.right(360/sides)
    
        
    
    

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.width(2)

colors = ["white", "red", "green", "pink", "blue", "yellow", "orange", "purple", "cyan", "aquamarine"]

for x in range(3):
    t.pencolor(colors[x])   
    t.penup()
    t.forward(100)
    t.pendown()
    for i in range(36):
        t.forward(2*i)
        t.right(90)
for x in range(100):
    t.pencolor(colors[3])   
    t.forward(x/2)
    t.right(12)
    
        
        
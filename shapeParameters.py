import turtle

def shape(a, b, c):
    t.pencolor(c)
    for x in range(a):
        t.forward(b)
        t.right(360/a)

t = turtle.Pen()
t.width(2)
turtle.bgcolor("black")
sides = int(input("number of sides: "))
size = int(input("size of shape: "))
print("colors: red, green, cyan, purple, white")
color = input("enter color: ")
shape(sides, size, color)
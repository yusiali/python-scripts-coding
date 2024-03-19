import turtle


def circle():
    for x in range(36):
        t.forward(1)
        t.right(10)


def triangle():
    for x in range(3):
        t.forward(20)
        t.right(120)


def square():
    for x in range(4):
        t.forward(20)
        t.right(90)


def pentagon():
    for x in range(5):
        t.forward(20)
        t.right(72)


t = turtle.Pen()
turtle.bgcolor("black")
t.width = 2
t.color("white")
go = "y"
while go == "y":
    print("circle:   1")
    print("triangle: 2")
    print("square:   3")
    print("pentagon: 4")
    shape = int(input("enter shape number: "))
    if shape == 1:
        circle()
    if shape == 2:
        triangle()
    if shape == 3:
        square()
    if shape == 4:
        pentagon()
    go = input("do u want to continue?('y' or 'n'): ")

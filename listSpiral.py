import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.width(1)

colors = []
colors = ["white", "red", "green", "pink", "blue", "yellow", "orange", "purple", "cyan", "aquamarine"]
#print(colors)
sides = (int(input("number of sides (max 10): ")))

for x in range(sides):
    colors.append(input("Enter a color: "))

for x in range(36):
    t.pencolor(colors[x % sides])
    t.forward(2 * x)
    t.right(360 / sides)
        
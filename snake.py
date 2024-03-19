from turtle import *
from random import randrange
from freegames import square, vector
food = vector(0,0)
snake = vector(10,0)
aim = vector(0, -10)
def change(x,y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x <200 and -200 < head.y < 200

def move():
    head = snake(-1).copy
    if not inside(head) or head in snake:
        square(head.x, head.y, 10, 'red')
        update()
        snake.append(head)
    if head == food:
        print(len(snake))
        food.x = randrange(-150, 150)
        food.y = randrange(-150, 150)
    else:
        snake.pop(0)   
    for body in snake:
        square(body.x, body.y, 10, 'black')
        
    square(head.x, head.y, 10, 'green')
    update()
    ontimer(move, 100)
    

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda : change(10,0), 'Right')
onkey(lambda : change(-10,0), 'Left')
onkey(lambda : change(0,10), 'Up')
onkey(lambda : change(0,-10), 'Down')
move()
done()


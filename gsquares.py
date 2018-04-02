import turtle
import random


bob = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
turtle.tracer(0)
turtle.colormode(255)

y = 403

def drawsquare(t,length,color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()



def randcolor():
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    randomcolor = (red , blue , green)
    
    return randomcolor


def moveturtle(t,x,y):
    t.pu()
    t.goto(x, y)
    t.pd()



for collum in range(80):
    moveturtle(bob, -480, y)
    for row in range(96):
        drawsquare(bob,10,randcolor())
        bob.forward(10)

    y = y - 10


wn.exitonclick()
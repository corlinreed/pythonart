import turtle, random

wn = turtle.Screen()
wn.bgcolor("black")
bob = turtle.Turtle()
bob.pensize(10)
wn.colormode(255)
bob.speed(0)
turtle.tracer(0)
wn.screensize(10000,10000)






def randomturn():
    turn = random.randint(0,360)

    return turn


def randcolor():
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    randomcolor = (red , blue , green)
    
    return randomcolor


def randomforward():
    forward = random.randint(0,100)

    return forward




for i in range(1000):
    bob.pencolor(randcolor())
    bob.right(randomturn())
    bob.forward(randomforward())

wn.exitonclick()
import turtle, random

wn = turtle.Screen()
wn.bgcolor("black")
turtle.tracer(0)
turtle.colormode(255)
t = turtle.Turtle()

def randcolor():
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    randomcolor = (red , blue , green)
    
    return randomcolor

for x in range(500):
    t.pencolor(randcolor())
    t.fd(x)
    t.rt(x)

wn.exitonclick()

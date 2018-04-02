import turtle, random

wn = turtle.Screen()
wn.bgcolor("black")
turtle.colormode(255)
t = turtle.Turtle()

def randcolor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    randomcolor = (red , green, blue)
    
    return randomcolor

for x in range(300):
    t.pencolor(randcolor())
    t.fd(20-(x/50))
    t.rt(x)

wn.exitonclick()

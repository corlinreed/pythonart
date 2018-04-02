import turtle

wn = turtle.Screen()
t = turtle.Turtle()

def hexagon(size):
    for x in range(6):
        t.fd(size)
        t.rt(60)

def stickfig(size):
    t.rt(180)
    hexagon(size)
    t.fd(size/2)
    t.lt(90)
    t.fd(size*2)
    t.rt(180)
    t.fd(size)
    t.rt(90)
    t.fd(size/2)
    t.bk(size)
    t.fd(size/2)
    t.rt(90)
    t.fd(size)
    t.rt(60)
    t.fd(size)
    t.bk(size)
    t.lt(120)
    t.fd(size)
    t.bk(size)
    

stickfig(50)

wn.exitonclick()
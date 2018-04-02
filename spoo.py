import turtle, random

wn = turtle.Screen()
wn.bgcolor("black")
t = turtle.Turtle()
t.pensize(3)
t.pencolor('orange')
wn.colormode(255)
t.speed(0)
turtle.tracer(0)

spooky_colors = ['orange', 'purple', 'orange', 'green']

def curve(segments, size, curvature):
	for x in range(segments):
		t.forward(size)
		t.right(curvature)

def triangle(size):
	t.rt(30)
	for x in range(3):
		t.fd(size)
		t.rt(120)


def pumpkin(size):
	t.pendown()
	t.right(180)
	for x in range(2):
		curve(90,(size/50),2)
		t.fd(size)
	t.penup()
	t.rt(90)
	t.fd(size*2/3)
	t.pendown()
	triangle(size/4)
	t.rt(60)
	t.penup()
	t.fd(size*3/4)
	t.left(90)
	t.pendown()
	triangle(size/4)
	t.penup()
	t.lt(120)
	t.fd(size*(3/8))
	t.lt(90)
	t.fd(size/4)
	t.rt(180)
	t.pendown()
	triangle(size/6)
	t.lt(120)
	t.penup()
	t.fd(size/3)
	t.pendown()
	t.rt(210)
	curve(90,(size/100),-.5)
	t.penup()

for n in range(random.randint(7,13)):
	pumpkin(random.randint(50,150))
	t.rt(random.randint(0,120))
	t.fd(random.randint(150,200))
	t.pencolor(random.choice(spooky_colors))
	

wn.exitonclick()
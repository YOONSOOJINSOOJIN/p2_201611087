﻿import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.penup()
t2.goto(-100,100)
t2.pendown()
t2.fd(200)
t1.shape("turtle")
def keyup():
	t1.forward(50)
def keyback():
	t1.back(50)
def keyright():
	t1.right(50)
def keyleft():
	t1.left(50)
def mousegoto(x,y):
	t1.setpos(x,y)
	t1.pos=(x,y)
	if 0<x<50 and 95<y<105:
		print "Correct"
def addkeys():
	wn.onkey(keyup,"Up")
	wn.onkey(keyback,"Back")
	wn.onkey(keyright,"Right")
	wn.onkey(keyleft,"Left")
def addmouse():
	wn.onclick(mousegoto)
	
addkeys()
addmouse()
wn.listen()
turtle.mainloop()

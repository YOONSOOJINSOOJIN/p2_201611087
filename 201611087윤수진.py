import turtle

wn.bgpic("/Users/sujinyun/Desktop/myMaze.gif")

wn=turtle.Screen()

t1=turtle.Turtle()

t1.clear()

t1.shape("turtle")

t1.speed(3)


def keyup():
    pt=t1.pos()
    print "up",pt
    t1.write(pt)
    t1.forward(45)

def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    pt=t1.pos()
    print "down",pt
    t1.write(pt)
    t1.back(45)

def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q") 

    
def mousegoto(x,y):
    msg="mouse clicked {0} {1}".format(x,y)
    wn.title(msg)
    t1.setpos(x,y)

def addMouse():
    wn.onclick(mousegoto) 

def gamePlay():
    addKeys()
    wn.listen()
    addMouse()
    wn.listen()
    turtle.mainloop()


def lab10():
    gamePlay()

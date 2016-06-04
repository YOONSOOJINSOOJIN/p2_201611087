import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def Maze():
    t1.speed(5)
    t1.penup()
    t1.goto(-300,240)
    wn.colormode(255)
    t1.pencolor((100,0,100))
    t1.pendown()
    t1.circle(30)
    t1.pencolor("black")
    t1.penup()
    t1.goto(-300,300)
    t1.pendown()
    t1.fd(600)
    t1.right(90)
    t1.fd(540)
    t1.circle(30)
    t1.penup()
    t1.pencolor("black")
    t1.goto(330,-270)
    t1.right(90)
    t1.pendown()
    t1.fd(660)
    t1.right(90)
    t1.fd(540)
    t1.penup()
    wn.colormode(255)
    t1.pencolor((100,0,100))
    t1.goto(-300,240)
    t1.pendown()
    t1.right(90)
    t1.fd(200)
    t1.right(90)
    t1.fd(200)
    t1.right(90)
    t1.fd(100)
    t1.right(90)
    t1.fd(100)
    t1.penup()
    t1.goto(-250,190)
    t1.pendown()
    t1.back(460)
    t1.penup()
    t1.goto(-250,0)
    t1.pendown()
    t1.right(90)
    t1.fd(200)
    t1.left(90)
    t1.fd(250)
    t1.penup()
    t1.goto(-250,-100)
    t1.pendown()
    t1.right(90)
    t1.fd(100)
    t1.right(90)
    t1.fd(40)
    t1.penup()
    t1.fd(30)
    t1.pendown()
    t1.fd(40)
    t1.right(90)
    t1.fd(100)
    t1.penup()
    t1.goto(50,100)
    t1.pendown()
    t1.back(200)
    t1.penup()
    t1.goto(150,100)
    t1.pendown()
    t1.left(90)
    t1.fd(370)
    t2=turtle.Turtle()
    t2.shape("turtle")
    t2.pencolor("green")
    t2.home()
    t2.clear()
    t2.penup()
    t2.goto(-300,270)
    t2.pendown()
    
def gameOver():
    t2.ht()
    t2.pencolor("Red")
    t2.write("GAME OVER", align = "center", font = ("courier", 25, "bold"))

def keyup():
    t2.forward(20)

def keyleft():
    t2.left(45)

def keyright():
    t2.right(45)

def keydown():
    t2.back(20)

def mousegoto(x,y):
    t1.setpos(x,y)
    t1.pos=(x,y)
    if -300<x<300 and y==300:
        gameOver()
        print "GAME OVER"
    if -270<y<300 and x==300:
        gameOver()
        print "GAME OVER"
    if -330<x<330 and y==-270:
        gameOver()
        print "GAME OVER"
    if -270<y<330 and x==-330:
        gameOver()
        print "GAME OVER"
    if -300<x<-100 and y==240:
        gameOver()
        print "GAME OVER"
    if 40<y<240 and x==-100:
        gameOver()
        print "GAME OVER"
    if -100<x<-200 and y==40:
        gameOver()
        print "GAME OVER"
    if 40<y<140 and x==-200:
        gameOver()
        print "GAME OVER"
    if -270<y<190 and x==-270:
        gameOver()
        print "GAME OVER"
    if -250<x<-50 and y==0:
        gameOver()
        print "GAME OVER"
    if 0<y<250 and x==-50:
        gameOver()
        print "GAME OVER"
    if -250<x<-150 and y==-100:
        gameOver()
        print "GAME OVER"
    if -140<y<-100 and x==-150:
        gameOver()
        print "GAME OVER"
    if -210<y<-170 and x==-150:
        gameOver()
        print "GAME OVER"
    if -150<x<-250 and y==-210:
        gameOver()
        print "GAME OVER"
    if 50<x<250 and y==100:
        gameOver()
        print "GAME OVER"
    if -270<y<100 and x==150:
        gameOver()
        print "GAME OVER"


def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q") 
    

def addMouse():
    wn.onclick(mousegoto) 
    

def drawStarFill(size,color):
    angle = 144
    t1.fillcolor(color)
    t1.begin_fill()
    for side in range(5):
        t1.fd(size)
        t1.right(angle)
    t1.end_fill()
    t1.penup()
    t1.goto(-290,-200)
    t1.pendown()
    drawStarFill(40,"yellow")
    t1.penup()
    t1.goto(-150,90)
    t1.pendown()
    drawStarFill(40,"yellow")
    t1.penup()
    t1.goto(-200,-165)
    t1.pendown()
    drawStarFill(40,"yellow")
    t1.penup()
    t1.goto(240,-185)
    t1.pendown()
    drawStarFill(40,"yellow")
    
def TurtleGame():
    Maze()
    gameOver()
    addKeys()
    addMouse()
    drawStarFill()
    
TurtleGame()
turtle.mainloop()

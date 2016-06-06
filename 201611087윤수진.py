import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.shape("turtle")
t2.pencolor("green")
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
    t2.home()
    t2.clear()
    t2.penup()
    t2.goto(-300,270)
    t2.pendown()
def gameOver():
    t2.ht()
    t2.pencolor("Red")
    t2.write("GAME OVER", align = "center", font = ("courier", 25, "bold"))

def drawStarFill(size,color):
    angle = 144
    t1.fillcolor(color)
    t1.begin_fill()
    for side in range(5):
        t1.fd(size)
        t1.right(angle)
    t1.end_fill()
def star():
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
    t1.ht()

def keyup():
    t2.forward(20)
    t=t2.pos()
    if -300<t[0]<300 and t[1]==300:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<300 and t[0]==300:
        gameOver()
        print "GAME OVER"
    if -330<t[0]<330 and t[1]==-270:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<330 and t[0]==-330:
        gameOver()
        print "GAME OVER"
    if -300<t[0]<-100 and t[1]==240:
        gameOver()
        print "GAME OVER"
    if 40<t[1]<240 and t[0]==-100:
        gameOver()
        print "GAME OVER"
    if -100<t[0]<-200 and t[1]==40:
        gameOver()
        print "GAME OVER"
    if 40<t[1]<140 and t[0]==-200:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<190 and t[0]==-270:
        gameOver()
        print "GAME OVER"
    if -250<t[0]<-50 and t[1]==0:
        gameOver()
        print "GAME OVER"
    if 0<t[1]<250 and t[0]==-50:
        gameOver()
        print "GAME OVER"
    if -250<t[0]<-150 and t[1]==-100:
        gameOver()
        print "GAME OVER"
    if -140<t[1]<-100 and t[0]==-150:
        gameOver()
        print "GAME OVER"
    if -210<t[1]<-170 and t[0]==-150:
        gameOver()
        print "GAME OVER"
    if -150<t[0]<-250 and t[1]==-210:
        gameOver()
        print "GAME OVER"
    if 50<t[0]<250 and t[1]==100:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<100 and t[0]==150:
        gameOver()
        print "GAME OVER"
def keyleft():
    t2.left(45)

def keyright():
    t2.right(45)

def keydown():
    t2.back(20)
    t=t2.pos()
    if -300<t[0]<300 and t[1]==300:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<300 and t[0]==300:
        gameOver()
        print "GAME OVER"
    if -330<t[0]<330 and t[1]==-270:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<330 and t[0]==-330:
        gameOver()
        print "GAME OVER"
    if -300<t[0]<-100 and t[1]==240:
        gameOver()
        print "GAME OVER"
    if 40<t[1]<240 and t[0]==-100:
        gameOver()
        print "GAME OVER"
    if -100<t[0]<-200 and t[1]==40:
        gameOver()
        print "GAME OVER"
    if 40<t[1]<140 and t[0]==-200:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<190 and t[0]==-270:
        gameOver()
        print "GAME OVER"
    if -250<t[0]<-50 and t[1]==0:
        gameOver()
        print "GAME OVER"
    if 0<t[1]<250 and t[0]==-50:
        gameOver()
        print "GAME OVER"
    if -250<t[0]<-150 and t[1]==-100:
        gameOver()
        print "GAME OVER"
    if -140<t[1]<-100 and t[0]==-150:
        gameOver()
        print "GAME OVER"
    if -210<t[1]<-170 and t[0]==-150:
        gameOver()
        print "GAME OVER"
    if -150<t[0]<-250 and t[1]==-210:
        gameOver()
        print "GAME OVER"
    if 50<t[0]<250 and t[1]==100:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<100 and t[0]==150:
        gameOver()
        print "GAME OVER"
    
def mousegoto(x,y):
    t2.setpos(x,y)
    t2.pos=(x,y)
    t=t2.pos()
    if -300<t[0]<300 and t[1]==300:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<300 and t[0]==300:
        gameOver()
        print "GAME OVER"
    if -330<t[0]<330 and t[1]==-270:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<330 and t[0]==-330:
        gameOver()
        print "GAME OVER"
    if -300<t[0]<-100 and t[1]==240:
        gameOver()
        print "GAME OVER"
    if 40<t[1]<240 and t[0]==-100:
        gameOver()
        print "GAME OVER"
    if -100<t[0]<-200 and t[1]==40:
        gameOver()
        print "GAME OVER"
    if 40<t[1]<140 and t[0]==-200:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<190 and t[0]==-270:
        gameOver()
        print "GAME OVER"
    if -250<t[0]<-50 and t[1]==0:
        gameOver()
        print "GAME OVER"
    if 0<t[1]<250 and t[0]==-50:
        gameOver()
        print "GAME OVER"
    if -250<t[0]<-150 and t[1]==-100:
        gameOver()
        print "GAME OVER"
    if -140<t[1]<-100 and t[0]==-150:
        gameOver()
        print "GAME OVER"
    if -210<t[1]<-170 and t[0]==-150:
        gameOver()
        print "GAME OVER"
    if -150<t[0]<-250 and t[1]==-210:
        gameOver()
        print "GAME OVER"
    if 50<t[0]<250 and t[1]==100:
        gameOver()
        print "GAME OVER"
    if -270<t[1]<100 and t[0]==150:
        gameOver()
        print "GAME OVER"
        
def eatStar():
    x1=coord[0][1]
    x2=coord[1][0]
    y1=coord[0][1]
    y2=coord[1][1]
    xs=min(-320,-260)
    xe=max(-320,-260)
    ys=min(-230,-170)
    ye=max(-230,-170)
    xs=min(-180,-120)
    xe=max(-180,-120)
    ys=min(60,120)
    ye=max(60,120)
    xs=min(-230,-170)
    xe=max(-230,-170)
    ys=min(-195,-135)
    ye=min(-195,-135)
    xs=min(210,270)
    xe=max(210,270)
    ys=min(-215,-155)
    ye=max(-215,-155)

        

def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.listen()

def addMouse():
    wn.onclick(mousegoto) 

    
    
def TurtleGame():
    Maze()
    addKeys()
    star()
    eatStar()
    addMouse()
TurtleGame()
turtle.mainloop()

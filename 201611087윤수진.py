import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.shape("turtle")
t2.pencolor("green")
gover=turtle.Turtle()
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
    

def drawStarFill(size,color):
    angle = 144
    t1.fillcolor(color)
    t1.begin_fill()
    for side in range(5):
        t1.fd(size)
        t1.right(angle)
    t1.end_fill()
    
def Star():
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

def up():
    t2.setheading(90)

def down():
    t2.setheading(270)

def left():
    t2.setheading(180)

def right():
    t2.setheading(0)

    
def mousegoto(x,y):
    t2.setpos(x,y)
    t2.pos=(x,y)
    t=t2.pos()
    

def addKeys():
    wn.onkey(up, "Up")
    wn.onkey(left, "Left")
    wn.onkey(right, "Right")
    wn.onkey(down, "Down")
    wn.listen()



def gameOver():
    gover.ht()
    gover.pencolor("Red")
    gover.write("GAME OVER", align = "center", font = ("courier", 25, "bold"))

    
    
def TurtleGame():
    Maze()
    Star()
    addKeys()
    speed=2
    while True:
        t2.fd(speed)

        if t2.xcor() < -300 or t2.xcor() > 300:
            gameOver()
            t2.ht()

            
        elif t2.ycor() < -300 or t2.ycor() > 300:
            gameOver()
            t2.ht()

       
 
       
TurtleGame()
turtle.mainloop()

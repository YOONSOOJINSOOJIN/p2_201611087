import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

def drawSquareAt(size, pos):

    t1.penup()

    t1.setpos(pos)

    t1.pendown()

    tracks=list()

    for i in range(0,4):

        tracks.append(t1.pos())

        t1.forward(size)

        t1.right(90)

    return tracks

def lab7():

    mytracks=drawSquareAt(100,(0,0))

    print mytracks

    

def main():

    lab7()

 

main()





import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

tracks=dict()

def drawSquareFrom():

    global tracks

tracks=({1:(100,0),2:(100,100),3:(0,100),4:(0,0)})

def lab7():

    for i in range(1,5):

        t1.goto(tracks[i])

def main():

    lab7()

    

main()

    

wn.exitonclick()

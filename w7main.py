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


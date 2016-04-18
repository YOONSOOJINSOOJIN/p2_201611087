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

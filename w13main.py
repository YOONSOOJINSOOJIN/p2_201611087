import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

import os

mydir=os.getcwd()

filename='Python.txt'

myfilename=mydir+'\\'+filename

myfilename=os.path.join(mydir,filename)

myfilehandle=open(myfilename)

myfilehandle.close()

 

def read1():

    try:

        fin1=open('Python.txt','a')

        fin2=open('outputNumber.txt','r')

        for line in fin2:

            fin1.write(line)

        fin1.close()

        fin2.close()

    except Exception as e:

        print e

 

def read2():

    try:

        fin1=open('Python.txt','a')

        fin2=open('outputNumber.txt','r')

        for line in fin2:

            fin1.write(line)

        fin1.close()

        fin2.close()

    except Exception as e:

        print e

    myfilehandle=open(myfilename)

    for line in myfilehandle:

        print line

    myfilehandle.close()

    

fres=open('reccords.txt')

mycoords=[]

for line in fres:

    line1=line.split(',')

    mycoords.append([(line1[0],line[1]),(line1[2],line1[3].strip())])

fres.close()    

    

 

 

def drawSquareWithCoords(coords):

    for coord in coords:

        x1=int(coord[0][0])

        x2=int(coord[1][0])

        y1=int(coord[0][1])

        y2=int(coord[1][1])

        print x1,y1,x2,y2

        t1.penup()

        t1.setpos(x1,y1)

        t1.pendown()

        for i in range(4):

            t1.fd(x2-x1)

            t1.left(90)

        

drawSquareWithCoords(mycoords)

 

def lab13():

    print "error"

    read1()

    print "append"

    read2()

    drawSquareWithCoords(mycoords)

    

def main():

    lab13()

    

if __name__=="__main__":

    main()

    

raw_input()

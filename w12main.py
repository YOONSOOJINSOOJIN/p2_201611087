%%writefile Python.txt

Python is a widely used high-level, general-purpose, interpreted,

dynamic programming language.[23][24]

Its design philosophy emphasizes code readability, and

its syntax allows programmers to express concepts in fewer lines of code

than would be possible in languages such as C++ or Java.[25][26]

The language provides constructs intended to enable clear programs on

both a small and large scale.[27]





import os

mydir=os.getcwd()




def wordprint():



    filename=raw_input("Python.txt")

    myfilename=os.path.join(mydir,filename)

    try:

        myfile=open(myfilename,'r')

        contents=myfile.readlines()

        for i in range(0,len(contents)):

            if contents[i].find('Python')>= 0:

                print contents[i]

        myfile.close()

    except IOError as e:

        print e

print wordprint()




def smallbig():

    myfilej=open('output.txt','w')

    line1='first line\n'

    myfilej.write(line1)

    line2='second line\n'

    myfilej.write(line2)

    line3='third line\n'

    myfilej.write(line3)

    line4='fourth line\n'

    myfilej.write(line4)

    line5='fifth line'

    myfilej.write(line5)

    myfilej.close()

    myfilej=open('output.txt','r')

    contentsj=myfilej.readlines()

    for a in range(0,len(contentsj)):

        if contentsj[a].find('l') >= 0:

            result = contentsj[a].split()

        for b in range(0,len(result)):

            if result[b].find('l') >= 0:

                print result[b].upper()

    myfilej.close()

print smallbig()




def lab12():

    wordprint()

    smallbig()

    

def main():

    lab12()

    

if __name__=="__main__":

    main()
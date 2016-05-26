import time

def msg():   

    myfile=open('output.txt','w')

    line1='first line\n'

    myfile.write(line1)

    line2='\t\tsecond line\n'

    myfile.write(line2)

    line3='third'

    myfile.write(line3)

    myfile.close()

    fin=open('output.txt','r')

    fout=open('outputUpper.txt','w')

    for line in fin:

        words=line.split()

        for word in words:

            if word=='line':

                word=word.upper()

                word+='[ysj edited {0}]'.format(time.strftime('%Y-%m-%d %H:%M:%S'))

                fout.write(word)

        print word

        fout.write('\n')

    fin.close()

    fout.close()

print msg

 

def data():

    data=[1,2,3,4,5,6,7,8,9,10]

    fout=open('outputNumber.txt','w')

    for i in data:

        str="{0}\t".format(i)

        if not i%2:

            str=str+'\n'

        fout.write(str)

    fout.close()

    

print data()

 

def lab13():

    msg()

    data()

    

def main():

    lab13()

    

if __name__=="__main__":

    main()

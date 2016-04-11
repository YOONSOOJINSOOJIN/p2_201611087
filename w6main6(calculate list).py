def totalList(x):

    y=list()

    for i in range(0,x):

        if (i%4==0 and not i%5==0):

            y.append(i)

            

    total=0

    for i in range(0,len(y)):

        total+=y[i]

    return total

    print total

    

def lab6():

    print """201611087 yoonsoojin homework"""

    x=1000

    labtotal=totalList(x)

    print labtotal

    

def main():

    lab6()

main()

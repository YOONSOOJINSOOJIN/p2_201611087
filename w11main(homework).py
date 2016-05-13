def Satisfaction():

    sa=list()

    sa=[["Division","Very satisfied","satisfied","dissatisfied","Very dissatisfied"],["Class quality",13.1,37.1,8.7,1.5

        ],["teaching method",10.6,34.6,13.4,1.9],["Friendship",27.1,40.0,2.9,1.5],["Teacher relation",16.2,37.8,6.8,0.8],

       ["School facility",11.4,29.8,14.8,4.9],["School environment",12.2,26.5,14.9,4.4],

        ["Major",13.5,29.7,11.1,2.4],["School life",13.7,37.6,4.1,1.2]]

    sa2=sa[1:]

    sum=0

    for i in sa2:

        sum1=i[1]+i[2]

        sum+=sum1

    sum2=0

    for i in sa2:

        sum3=i[3]+i[4]

        sum2+=sum3

    SatisfiedAverage=sum/len(sa2)

    DissatisfiedAverage=sum2/len(sa2)

    

    print "Satisfied average is "+str(SatisfiedAverage)

    print "Dissatisfied average is "+str(DissatisfiedAverage)

 

def lab11():

    Satisfaction()

def main():

    lab11()

 

if __name__=="__main__":

    main()

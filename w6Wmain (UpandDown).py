def UpandDown():

    soojin1=raw_input("Please write number : ")

    opportunity=raw_input("Please determine opportunity number : ")

    opportunity=int(opportunity)

    for i in range(opportunity):

        soojin1=int(soojin1)

        soojin2=raw_input("Please write number : ")

        soojin2=int(soojin2)

        if soojin1>soojin2:

            print "Up"

        elif soojin1<soojin2:

            print "Down"

        elif soojin1==soojin2:

            print "Good!"

            break

        print "Game over"

 

UpandDown()

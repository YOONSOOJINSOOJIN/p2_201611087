def Presidentspeech():

    def Georgespeech():

        Georgespeech=list()

        Georgespeech=["On this day, prescribed by law and marked by ceremony, we celebrate the durable wisdom of our Constitution, and recall the deep commitments that unite our country. I am grateful for the honor of this hour, mindful of the consequential times in which we live, and determined to fulfill the oath that I have sworn and you have witnessed."

                      "At this second gathering, our duties are defined not by the words I use, but by the history we have seen together. For a half century, America defended our own freedom by standing watch on distant borders. After the shipwreck of communism came years of relative quiet, years of repose, years of sabbatical."

                      "We have seen our vulnerability —and we have seen its deepest source. For as long as whole regions of the world simmer in resentment and tyranny —prone to ideologies that feed hatred and excuse murder — violence will gather, and multiply in destructive power, and cross the most defended borders, and raise a mortal threat." 

                      "There is only one force of history that can break the reign of hatred and resentment, and expose the pretensions of tyrants, and reward the hopes of the decent and tolerant, and that is the force of human freedom."]

        doc=Georgespeech

        d=dict()

        for i in range(len(doc)):

            for c in doc[i].split():

                if c not in d:

                    d[c]=1

                

                else:

                    d[c]+=1

        for s in range(len(d)):

            if d.values()[s]>3:

                print d.keys()[s],d.values()[s]

        a=list()

        for i in d.values():

            a.append(i)

        b=list()

        c=list()

        for i in d.keys():

            b.append(i)

        for i in range(len(a)):

            if a[i]>=24:

                c.append(b[i])

        print"George was likely to say words"+str(c)+"in his speech"

    

    def Johnspeech():

        Johnspeech=list()

        Johnspeech=["WHEN it was first perceived, in early times, that no middle course for America remained between unlimited submission to a foreign legislature and a total independence of its claims, men of reflection were less apprehensive of danger from the formidable power of fleets and armies they must determine to resist than from those contests and dissensions which would certainly arise concerning the forms of government to be instituted over the whole and over the parts of this extensive country.",

                      "Relying, however, on the purity of their intentions, the justice of their cause, and the integrity and intelligence of the people, under an overruling Providence which had so signally protected this country from the first, the representatives of this nation, then consisting of little more than half its present number, not only broke to pieces the chains which were forging and the rod of iron that was lifted up, but frankly cut asunder the ties which had bound them, and launched into an ocean of uncertainty.",

                      "The zeal and ardor of the people during the Revolutionary war, supplying the place of government, commanded a degree of order sufficient at least for the temporary preservation of society. The Confederation which was early felt to be necessary was prepared from the models of the Batavian and Helvetic confederacies, the only examples which remain with any detail and precision in history, and certainly the only ones which the people at large had ever considered.",

                      "But reflecting on the striking difference in so many particulars between this country and those where a courier may go from the seat of government to the frontier in a single day, it was then certainly foreseen by some who assisted in Congress at the formation of it that it could not be durable."]

        doc=Johnspeech

        d=dict()

        for i in range(len(doc)):

            for c in doc[i].split():

                if c not in d:

                    d[c]=1

                else:

                    d[c]+=1

        for s in range(len(d)):

            if d.values()[s]>3:

                print d.keys()[s],d.values()[s]

        a=list()

        for i in d.values():

            a.append(i)

        b=list()

        c=list()

        for i in d.keys():

            b.append(i)

        for i in range(len(a)):

            if a[i]>=3:

                c.append(b[i])

        print "George was likely to say words"+str(c)+"in his speech"

 

def Presidentspeech():

    Georgespeech()

    Johnspeech()

    

def lab11():

    Presidentspeech()

def main():

    lab11()

 

if__name__=="__main__":

    main()

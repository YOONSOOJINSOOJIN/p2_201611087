import matplotlib

import matplotlib.pyplot as plt

myList=list()

mylist=[

    [74425,76326],

    [61164,61636],

    [109688,115744],

    [144796,146776],

    [174996,181676],

    [177841,177434],

    [204630,205980],

    [223373,232245],

    [161055,166130],

    [171576,176735],

    [279169,293772],

    [239450,251066],

    [148690,156510],

    [182977,196992],

    [237792,242641],

    [283869,296762],

    [209344,210282],

    [118965,114441],

    [186503,186856],

    [195734,203014],

    [254381,249472],

    [212401,229111],

    [271654,295354],

    [319197,335045],

    [229829,231671]

]

def manwomansumaverage():

    man=0

    woman=0

    for i in range(0,len(myList)):

        man=man+myList[i][0]

        woman=woman+myLisst[i][1]

    print "man's sum"

    print man

    print "An average man"

    print man/len(myList)

    print "woman's sum"

    print woman

    print "An average woman"

    print woman/len(myList)

 

jr=(74425,76326)

jg=(61164,61636)

ys=(109688,115744)

sd=(144796,146776)

gj=(174996,181676)

ddm=(177841,177434)

jra=(204630,205980)

sb=(223373,232245)

gb=(161055,166130)

db=(171576,176735)

nw=(279169,293772)

ep=(239450,251066)

sdm=(148690,156510)

mp=(182977,196992)

yc=(237792,242641)

gs=(283869,296762)

gr=(209344,210282)

gc=(118965,114441)

ydp=(186503,186856)

dj=(195734,203014)

ga=(254381,249472)

sc=(212401,229111)

gn=(271654,295354)

sp=(319197,335045)

gd=(229829,231671)

 

Locations={"jr","jg","ys","sd","gj","ddm","jra","sb","gb","db","nw","ep","sdm","mp","yc","gs","gr","gc","ydp","dj","ga","sc","gn","sp","gd"}

 

d=dict()

def graph():

    for i in Locations:

        d[str(i)]=gu[i][0]+Loc[i][1]

    plt.bar(range(len(d)),d.values(), align='center')

    plt.xticks(range(len(d)), list(d.keys()))

    plt.show()

 

    

def lab9():

    manwomansumaverage()

    graph()

    

def main():

    lab9()

    

    main()

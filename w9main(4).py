ky=(37.576119, 126.973580)

kw=(37.571853, 126.976457)

an=(37.576569, 126.985461)

dok=(37.574487, 126.957961)

jon=(37.570173, 126.983142)

def nearbystation():

    Locations=tuple()

    Locations=((37.571853, 126.976457),(37.576569, 126.985461),(37.574487, 126.957961),(37.570173, 126.983142))

    import math

    distanceex=math.sqrt((1-3)**2+(2-4)**2)

    print Locations[0][0]

    for i in Locations:

        print "x={0},y={1}".format(i[0],i[1])

        name='jsl'

        place='home'

    ky=(37.576119, 126.973580)

    distance=list()

    for t in Locations:

        distance=math.sqrt((ky[0]-t[0])**2+(ky[1]-t[1])**2)

        print "distance: ", distance

        Locations.append(distance)

        print "the minimum distance is ", min(dist)

        

def lab9():

    nearbystation()

    

def main():

    lab9()

    

    main()

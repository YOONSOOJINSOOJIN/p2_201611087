myhome=set()

friendshome=set()

myhome={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light' , 'computer', 'notebook', 'recorder'}

friendshome={'coffee', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}

 

def myhome():

    print myhome.difference(friendshome)

def friendshome():

    print friendshome.difference(myhome)

def together():

    print myhome.intersection(friendshome)

def All():

    print myhome.union(friendshome)

def count():

    d=dict()

    for c in myhome:

        if c not in d:

            d[c]=1

        else:

            d[c]=d[c]+1

    for c in friendshome:

        if c not in d:

            d[c]=1

        else :

            d[c]=d[c]+1

    print d 

 

    

def lab9():

    myhome()

    friendshome()

    together()

    All()

    count()

    

def main():

    lab9()

    

 

    

    main()

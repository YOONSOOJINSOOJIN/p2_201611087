def charCount():

    sentence= 'sangmyung university'

    print list(sentence)

    allchars=list(sentence)

    for c in allchars:

        print c,

    d=dict()

    for c in allchars:

        if c not in d:

            d[c]=1

    else:

            d[c]=d[c]+1

    print d

    import matplotlib

    import matplotlib.pyplot as plt

 

    plt.bar(range(len(d)),d.values(), align='center')

    plt.xticks(range(len(d)), list(d.keys()))

    plt.show()

 

def main():

    lab9()

    

    main()

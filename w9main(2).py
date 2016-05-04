def countDigitalsLetters(word):

    setence="7 honggildong"

    allchars=list(sentence)

    d=dict()

    d={"number":0, "word":0}

    for c in word:

        if countDigitalsLetters()==True:

            d["number"]=d["number"]+1

        elif countDigitalsLetters()==False:

            d["word"]=d["word"]+1

    print d

    

    import matplotlib

    import matplotlib.pyplot as plt

    plt.bar(range(len(d)),d.values(), align='center')

    plt.xticks(range(len(d)), list(d.keys()))

    plt.show()

 

def lab9():

    countDigitalsLetters(word)

    

def main():

    lab9()

    

 

    main()

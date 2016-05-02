sentence= 'sangmyung university'
print sentence.split()
print list(sentence)
allchars=list(sentence)
print allchars
for c in allchars:
    print c,
print allchars[1]
d=dict()
d['a']=1
d['b']=1
d['b']+=1
print d
print 'a' in d
print 'b' in d
sentence= 'sangmyung university'
d=dict()
for c in sentence:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1
print d
print len(d)
print d.keys()
print d.values()

import matplotlib
import matplotlib.pyplot as plt

plt.bar(range(len(d)),d.values(), align='center')
plt.xticks(range(len(d)), list(d.keys()))
plt.show()

def main()
    lab9()
    
main()
wn.exitonclick()

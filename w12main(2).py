def msg():   
    msg='[ysj edited {0}]'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
print msg()
 
def data():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('outputNumber.txt','w')
    for i in data:
        str="{0}\t".format(i)
        if not i%2:
            str=str+'\n'
        fout.write(str)
    fout.close()
    
print data()
 
def lab12():
    msg()
    data()
    
def main():
    lab12()
    
if __name__=="__main__":
    main()

def MilkProportion():

    allData=list()

    allData=[ ["Coffee","Water","Milk","Icecream"],

    ["Espresso","No","No","No"],

    ["Long Black","Yes","No","No"],

    ["Flat White","No","Yes","No"],

    ["Cappuccino","No","Yes-Frothy","No"],

    ["Affogato","No","No","Yes"]

    ]

	data=allData[1:] 

	for i in range(0,len(data)):

		print data[i][2]

	for i in data:

		print i[2]

	a=0

	for i in data:

		if i[2]=="No":

			a=a

		else:

			a=a+1

	print 'milk proportion'

	result=(100*a/len(data))

	print result, "%"

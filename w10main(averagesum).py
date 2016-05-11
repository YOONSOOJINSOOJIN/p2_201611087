def averagesum():

    marks=list()

    marks=[["English",100],

            ["Math",200],

          ["English",200],

          ["Math",200],

          ["English",100],

          ["Math",300]

    ]

	a=0

	d=0

	m=0

	e=0

	for i in range(len(marks)):

		if marks[i][0]=="English":

			e=e+1

		else:

			e=e

	for i in range(len(marks)):

		if not i%2:

			d=d+marks[i][1]

		else:

			m=m+marks[i][1]

	result1=(d/e)

	result2=(m/(len(marks)-e))

	print 'English'

	print result1

	print 'Math'

	print result2

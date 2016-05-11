def words():

	lyrics=list()

	lyrics=["When I find myself in times of trouble",

		"Mother Mary comes to me",

		"Speaking words of wisdom let it be",

		"And in my hour of darkness",

		"She is standing right in front of me",

    		"Speaking words of wisdom let it be",

    		"Let it be let it be",

 		"Let it be let it be",

    		"Whisper words of wisdom let it be",

    		"And when the broken-hearted people",

    		"Living in the world agree",

    		"There will be an answer let it be",

    		"For though they may be parted",

    		"There is still a chance that they will see",

    		"There will be an answer let it be",

    		"Let it be let it be",

    		"Let it be let it be",

    		"Yeah there will be an answer let it be",

    		"Let it be let it be",

    		"Let it be let it be",

    		"Whisper words of wisdom let it be"]

	doc=lyrics

	for sentence in doc:

		words=sentence.split()

    	for word in words:

		print word,

	word = 'doc'

	d = dict()

	for i in sentence.split():

		if i not in d:

			d[i]=1

		else:

			d[i]=d[i]+1

	print "단어",d

	for v in range(len(d)):

	if d.values()[v]>=20:

	print d.keys()[v], d.values()[v]

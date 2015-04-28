with open("../out/dataset_withID_with_phrases.csv") as fd:
	lastid = lastphrase = None
	i=1
	for line in fd:
		splittedLine = line.split(',',maxsplit=2)
		idm=int(splittedLine[0])
		phrase=int(splittedLine[1])
		
		if i>1:
			if idm-lastid>=1:
				if phrase-lastphrase>=1:
					print('error at line '+i)
				else:
					correctphrase=0

		if 

		lastid=idm
		correctphrase+=1
		i+=1
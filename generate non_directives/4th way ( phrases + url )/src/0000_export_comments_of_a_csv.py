#fdout = open('../possible_directives_(comments_with_keywords)(only comments).csv','w')
fdout = open('../dataset_withID_without_directives_(only comments).csv','w')

linesNotCorrectlyFormated = 0
#with open('../possible_directives_(comments_with_keywords).csv') as fdin:
with open('../dataset_withID_without_directives.csv') as fdin:
	for line in fdin:
		splitted = line.split(',',3)
		if len(splitted) == 4:
			fdout.write(splitted[3])
		else:
			linesNotCorrectlyFormated += 1

print('linesNotCorrectlyFormated='+str(linesNotCorrectlyFormated))
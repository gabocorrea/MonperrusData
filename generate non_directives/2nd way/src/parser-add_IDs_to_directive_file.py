fdAll = open("../data/datasetWithNoExtraSymbols-out.csv")
fdDirectives = open("../data/directives_only_the_comments_WithNoExtraSymbols.csv")
fdDirectivesOriginal = open("../data/directive.csv")
fdout = open("../out/directives_withID_onlyComments.csv","w")
fdoutModifiedDirectives = open("../out/directives_withID.csv","w")

log = open("../out/log.txt","w")
i = 0

myList = []

SetWithTheLinesAlreadyVisited = set()


def searchStringInAlreadyOpenedFile(searchStr, fileDescriptor, setWithLinesExamined):
	"""Returns the line number (an int) where it found searchStr in the fileDescriptor. 
	Returns False if not found. No repeated lines should be returned.. else it is reported on the log."""
	currentLineNumber = 1
	for line in fileDescriptor:
		if searchStr in line and currentLineNumber not in setWithLinesExamined:
			fileDescriptor.seek(0)
			setWithLinesExamined.add(currentLineNumber)
			return currentLineNumber
		currentLineNumber += 1
	fileDescriptor.seek(0)
	return False

directives_original_list = []
for line in fdDirectivesOriginal:
	directives_original_list.append(line)

fdoutModifiedDirectives.write("id,"+directives_original_list[0])

# fdDirectives is a CSV that contains a directive comment in each line
#### ******* warning: this assumes fdinDirectives and fdoutModifiedDirectives have the same number of lines, and same order
for line in fdDirectives:
	if i%100 == 0:
		print(i)

	# we dont consider last two characters which are a comma and a newline
	n = searchStringInAlreadyOpenedFile(line[:-2], fdAll, SetWithTheLinesAlreadyVisited)
	if n is False:
		if i<len(directives_original_list):
			fdoutModifiedDirectives.write("-1,"+directives_original_list[i+1])
		myList.append("-1,"+line[:-1]+"\n")
	else:
		if i<len(directives_original_list):
			fdoutModifiedDirectives.write(str(n)+","+directives_original_list[i+1])
		myList.append(str(n)+","+line[:-1]+"\n")

	i += 1


log.write("\ndone! found "+str(len(myList)) + " matches")
fdout.write("id,commentText\n")
for elem in myList:
	fdout.write(elem)

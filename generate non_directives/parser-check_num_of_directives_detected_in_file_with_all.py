import re

fdAll = open("datasetWithNoExtraSymbols-out.csv")
fdDirectives = open("directives_only_the_comments.csv")
fdout = open("parser-check_num_of...-out.csv","w")
i = 0

doOnlyTenLoops = False
myList = []



def searchStringInAlreadyOpenedFile(searchStr, fileDescriptor):
	"""Returns the line number (an int) where it found searchStr in the fileDescriptor. 
	Returns False if not found"""
	currentLineNumber = 1
	for line in fileDescriptor:
		

		#if currentLineNumber < 5 :
		#	fdout.write(searchStr+"\n")
		#	fdout.write(line + "\n")
		#elif currentLineNumber == 5:
		#	fdout.write("______________________________\n\n")


		if searchStr in line:
			fileDescriptor.seek(0)
			return currentLineNumber
		currentLineNumber += 1
	fileDescriptor.seek(0)
	return False



# fdDirectives is a CSV that contains a directive comment in each line
for line in fdDirectives:
	if i%100 == 0:
		print(i)

	# we dont consider last two characters which are a comma and a newline
	n = searchStringInAlreadyOpenedFile(line[:len(line)-2], fdAll)
	if n == False:
		pass
	else:
		myList.append(n)
	i += 1


print("\ndone! found "+len(myList) + " matches")
fdout.write("[")
for elem in myList:
	fdout.write(str(elem)+",")
fdout.write("]\n")
for elem in myList:
	fdout.write(str(elem)+"\n")

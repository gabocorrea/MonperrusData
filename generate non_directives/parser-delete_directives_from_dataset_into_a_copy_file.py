import re

fdAll = open("datasetWithNoExtraSymbols-out.csv")
fdDirectives = open("directives_only_the_comments.csv")
fdout = open("parser-delete_directives_from_...-out.csv","w")
log = open("parser-delete_directives_from_...(deleted lines).txt","w")
i = 0

loops = 0 #put 0 for loop until end (infinite)
myList = []

class Counter:
	def __init__(self):
		self.counter = 0
	def add(self):
		self.counter += 1
	def get(self):
		return self.counter
	def set(self, intNumber):
		self.counter = intNumber
	def __str__(self):
		return str(self.counter)

deleteCount = Counter()

def checkIfStringOfDatasetHasADirectiveInTheFileWithDirectives(searchStr, fileDescriptor, counter):
	"""Returns the line number (an int) where it found searchStr in the fileDescriptor. 
	Returns False if not found"""
	for line in fileDescriptor:
		
		# we dont consider last two characters which are a comma and a newline
		lineSubstring = line[:len(line)-2]
		L = (lineSubstring+".")[0:-1]
		if lineSubstring in searchStr:
			log.write("1\n"+ L + "\n\n2\n" + searchStr + "\n_______________________________________\n")
			counter.add()

			fileDescriptor.seek(0)
			return True
	fileDescriptor.seek(0)
	return False

import math

# fdAll is the file with the dataset
for line in fdAll:
	if loops>0 and i%math.ceil(loops/10) == 0:
		print(i)
	elif loops==0 and i%1000:
		print(i)

	if loops>0 and i>=loops:
		break

	# we dont consider last two characters which are a comma and a newline
	n = checkIfStringOfDatasetHasADirectiveInTheFileWithDirectives(line, fdDirectives, deleteCount)
	if not n:
		fdout.write(line)
	else:
		pass
	i += 1


log.write("\n\ndone!\nlines deleted:"+str(deleteCount))

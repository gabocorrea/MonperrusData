import re

loops = 0 #put 0 for loop until end (infinite)


patternsStr = r"\bcall\w*\b" + r"|" + r"\binvo\w*\b" + r"|" + r"\bbefore\b" + r"|" + r"\bafter\b" + r"|" + r"\bbetween\b" + r"|" + r"\bonce\b" + r"|" + r"\bprior\b" + r"|" + r"\bmust\b" + r"|" + r"\bmandat\w*\b" + r"|" + r"\brequire\w*\b" + r"|" + r"\bshall\b" + r"|" + r"\bshould\b" + r"|" + r"\bencourage\w*\b" + r"|" + r"\brecommend\w*\b" + r"|" + r"\bmay\b" + r"|" + r"\bassum\w*\b" + r"|" + r"\bonly\b" + r"|" + r"\bdebug\w*\b" + r"|" + r"\brestrict\w*\b" + r"|" + r"\bnever\b" + r"|" + r"\bcondition\w*\b" + r"|" + r"\bstrict\w*\b" + r"|" + r"\bnecessar\w*\b" + r"|" + r"\bportab\w*\b" + r"|" + r"\bstrong\w*\b" + r"|" + r"\bperforman\w*\b" + r"|" + r"\befficien\w*\b" + r"|" + r"\bfast\b" + r"|" + r"\bquick\b" + r"|" + r"\bbetter\b" + r"|" + r"\bbest\b" + r"|" + r"\bconcurren\w*\b" + r"|" + r"\bsynchron\w*\b" + r"|" + r"\block\w*\b" + r"|" + r"\bthread\w*\b" + r"|" + r"\bsimultaneous\w*\b" + r"|" + r"\bdesir\w*\b" + r"|" + r"\balternativ\w*\b" + r"|" + r"\baddition\w*\b" + r"|" + r"\bextend\w*\b" + r"|" + r"\boverrid\w*\b" + r"|" + r"\boverload\w*\b" + r"|" + r"\boverwrit\w*\b" + r"|" + r"\breimplement\w*\b" + r"|" + r"\bsubclass\w*\b" + r"|" + r"\bsuper\w*\b" + r"|" + r"\binherit\w*\b" + r"|" + r"\bwarn\w*\b" + r"|" + r"\baware\w*\b" + r"|" + r"\berror\w*\b" + r"|" + r"\bnote\w*\b"

fdAllWithLessDirectives = open("parser-delete_directives_from_...-out.csv")
fdout = open("parser-pick_random_lines_without_...-out.csv","w")
fdout2 = open("parser-pick_random_lines_without_...-out(maybe_directives).csv","w")
#log = open("log.txt","w")

numOfLines = 0
for line in fdAllWithLessDirectives:
	numOfLines+=1
fdAllWithLessDirectives.seek(0)


i = 0

myList = []

p = re.compile(patternsStr, re.IGNORECASE)

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

import math


# fdAllWithLessDirectives is the file with the version of the dataset that had some of it's directives extracted
for line in fdAllWithLessDirectives:

	### ____ This code is to allow us to limit the lines analyzed using variable loops ____
	if loops>0 and i%math.ceil(loops/10) == 0:
		print(math.ceil(i/numOfLines*100), "%")
	elif loops==0 and i%math.ceil(numOfLines/10) == 0:
		print(math.ceil(i/numOfLines*100),"%")

	if loops>0 and i>=loops:
		break
	### (end)

	if p.search(line) == None:
		fdout.write(line)
	else:
		fdout2.write(line)


	i += 1
print(math.ceil(i/numOfLines*100), "%")

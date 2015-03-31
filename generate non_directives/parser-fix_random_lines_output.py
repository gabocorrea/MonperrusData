"""the output of parser-pick_random_lines_without_DirectiveKeywords.py didn't have "" simbols surrounding
each column of the .csv ... this script fixes that """

import re

loops = 0 #put 0 for loop until end (infinite)


patternsStr = r"\bcall\w*\b" + r"|" + r"\binvo\w*\b" + r"|" + r"\bbefore\b" + r"|" + r"\bafter\b" + r"|" + r"\bbetween\b" + r"|" + r"\bonce\b" + r"|" + r"\bprior\b" + r"|" + r"\bmust\b" + r"|" + r"\bmandat\w*\b" + r"|" + r"\brequire\w*\b" + r"|" + r"\bshall\b" + r"|" + r"\bshould\b" + r"|" + r"\bencourage\w*\b" + r"|" + r"\brecommend\w*\b" + r"|" + r"\bmay\b" + r"|" + r"\bassum\w*\b" + r"|" + r"\bonly\b" + r"|" + r"\bdebug\w*\b" + r"|" + r"\brestrict\w*\b" + r"|" + r"\bnever\b" + r"|" + r"\bcondition\w*\b" + r"|" + r"\bstrict\w*\b" + r"|" + r"\bnecessar\w*\b" + r"|" + r"\bportab\w*\b" + r"|" + r"\bstrong\w*\b" + r"|" + r"\bperforman\w*\b" + r"|" + r"\befficien\w*\b" + r"|" + r"\bfast\b" + r"|" + r"\bquick\b" + r"|" + r"\bbetter\b" + r"|" + r"\bbest\b" + r"|" + r"\bconcurren\w*\b" + r"|" + r"\bsynchron\w*\b" + r"|" + r"\block\w*\b" + r"|" + r"\bthread\w*\b" + r"|" + r"\bsimultaneous\w*\b" + r"|" + r"\bdesir\w*\b" + r"|" + r"\balternativ\w*\b" + r"|" + r"\baddition\w*\b" + r"|" + r"\bextend\w*\b" + r"|" + r"\boverrid\w*\b" + r"|" + r"\boverload\w*\b" + r"|" + r"\boverwrit\w*\b" + r"|" + r"\breimplement\w*\b" + r"|" + r"\bsubclass\w*\b" + r"|" + r"\bsuper\w*\b" + r"|" + r"\binherit\w*\b" + r"|" + r"\bwarn\w*\b" + r"|" + r"\baware\w*\b" + r"|" + r"\berror\w*\b" + r"|" + r"\bnote\w*\b"

fdin = open("parser-pick_random_lines_without_...-out.csv")
fdout = open("parser-fix_random_lines_...o-ut.csv","w")
#log = open("parser-pick_random_lines_without_...-(log).txt","w")

numOfLines = 0
for line in fdin:
	numOfLines+=1
fdin.seek(0)


i = 0


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

pos = 0

# fdAllWithLessDirectives is the file with the version of the dataset that had some of it's directives extracted
for line in fdin:

	### ____ This code is to allow us to limit the lines analyzed using variable loops ____
	if loops>0 and i%math.ceil(loops/10) == 0:
		print(i)
	elif loops==0 and i%math.ceil(numOfLines/10):
		print(i)

	if loops>0 and i>=loops:
		break
	### (end)

	#word = ""
	#p1 = line.find(",")
	#word += "\""+line[:p1]+"\",")
	#p2 = line.find(",",p1+1)
	#word += "\""+line[p1+1:p2]+"\""
	
	L = line.split(",",2)
	for j in range(3):
		if j==2:
			fdout.write("\""+L[j][:-1]+"\"\n")
		elif j<2:
			fdout.write("\""+L[j]+"\",")


	i += 1

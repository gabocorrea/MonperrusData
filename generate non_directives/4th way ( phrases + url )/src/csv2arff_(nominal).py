import re
import csv

#########	Modify these variables     ###########
fileIn_name = "dataset_withID_with_non_directives.csv"
sparce = False
##################################################



if "non_directives" in fileIn_name:
	is_directive = 0
elif "directives" in fileIn_name:
	is_directive = 1
else:
	import sys
	print("MyError: file_name var in line 4 of this script must be a string containing either 'non_directives' or 'directives' in it's name!")
	sys.exit()

patterns = [r"\bcall\w*\b" ,
 r"\binvo\w*\b" ,
 r"\bbefore\b" ,
 r"\bafter\b" ,
 r"\bbetween\b" ,
 r"\bonce\b" ,
 r"\bprior\b" ,
 r"\bmust\b" ,
 r"\bmandat\w*\b" ,
 r"\brequire\w*\b" ,
 r"\bshall\b" ,
 r"\bshould\b" ,
 r"\bencourage\w*\b" ,
 r"\brecommend\w*\b" ,
 r"\bmay\b" ,
 r"\bassum\w*\b" ,
 r"\bonly\b" ,
 r"\bdebug\w*\b" ,
 r"\brestrict\w*\b" ,
 r"\bnever\b" ,
 r"\bcondition\w*\b" ,
 r"\bstrict\w*\b" ,
 r"\bnecessar\w*\b" ,
 r"\bportab\w*\b" ,
 r"\bstrong\w*\b" ,
 r"\bperforman\w*\b" ,
 r"\befficien\w*\b" ,
 r"\bfast\b" ,
 r"\bquick\b" ,
 r"\bbetter\b" ,
 r"\bbest\b" ,
 r"\bconcurren\w*\b" ,
 r"\bsynchron\w*\b" ,
 r"\block\w*\b" ,
 r"\bthread\w*\b" ,
 r"\bsimultaneous\w*\b" ,
 r"\bdesir\w*\b" ,
 r"\balternativ\w*\b" ,
 r"\baddition\w*\b" ,
 r"\bextend\w*\b" ,
 r"\boverrid\w*\b" ,
 r"\boverload\w*\b" ,
 r"\boverwrit\w*\b" ,
 r"\breimplement\w*\b" ,
 r"\bsubclass\w*\b" ,
 r"\bsuper\w*\b" ,
 r"\binherit\w*\b" ,
 r"\bwarn\w*\b" ,
 r"\baware\w*\b" ,
 r"\berror\w*\b" ,
 r"\bnote\w*\b"]

class Debug:
	def __init__(self):
		self.NotUsed = True	
	def log(self, text):
		mode = "w" if self.NotUsed else "a"
		with open("../out/log.txt",mode) as fdlog:
			fdlog.write(str(text))
		if self.NotUsed: self.NotUsed=False
debug = Debug()

loops = 0 #put 0 for loop until end (infinite)


def getPatternCountList( text , regexList):
	""" Returns a list of ints """
	L=[]
	for regex in regexList:
		p = re.compile(regex, re.IGNORECASE)

		if p.search(text) == None:
			L.append(0)
		else:
			L.append(1)

	return L

def getPatternCountListSparse( text, regexList):
	""" Returns a list of strings """
	L=[]
	i=1
	for regex in regexList:
		p = re.compile(regex, re.IGNORECASE)

		if p.search(text) == None:
			pass
		else:
			L.append(str(i)+" "+str(1))
		i+=1
	return L


i=0
with open("../out/"+fileIn_name[:-3]+"arff","w") as fdout:
	fdout.write("% 1. Title: Directive Keywords present in file "+ fileIn_name +"\n\n")
	fdout.write("@RELATION directive_keywords\n\n")

	fdout.write("@ATTRIBUTE id NUMERIC")
	for elem in patterns:
		inicio = elem.find("b")+1
		fin = elem.find("\\", inicio)
		word = elem[inicio:fin]
		fdout.write("@ATTRIBUTE "+word+" NUMERIC\n")
	fdout.write("@ATTRIBUTE is_directive NUMERIC\n")
	fdout.write("\n@DATA\n")

	with open("../out/"+fileIn_name) as fdin:
		csvDictReader = csv.DictReader(fdin)
		for row in csvDictReader:

			if loops<1 and i%500==0:
				print(i+" lines scanned")
			if loops>=1 and i>=loops:
				break
			
			debug.log(str(type(row["text"]))+"\n")

			if not sparce:
				fdout.write(row["id"]+"," + ",".join(str(num) for num in getPatternCountList(str(row["text"]), patterns)) +","  +str(is_directive)+  "\n")
			else:
				fdout.write("{0 "+row["id"]+","  +  ",".join(words for words in getPatternCountListSparse(str(row["text"])))  +str(len(patterns)+2-1)+" "+str(is_directive)  "}\n")



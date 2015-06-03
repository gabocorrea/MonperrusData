import re
import csv

#########	Modify these variables     ###########
fileIn_name = "dataset_corrected.csv" #must be a .csv
#not used# is_directive = 1 #put 0 for a file without directives. 1 for a file with only directives
num_of_columns = 6 #1st column should be id. last column should be comment_text

sparce = False
##################################################


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
		with open("log.txt",mode) as fdlog:
			fdlog.write(str(text))
		if self.NotUsed: self.NotUsed=False
debug = Debug()



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

sparce_str_file_name = ''
if sparce:
	sparce_str_file_name = '_(sparce)'
with open(fileIn_name[:-4]+sparce_str_file_name+".arff","w") as fdout:
	fdout.write("% 1. Title: Directive Keywords present in file "+ fileIn_name +"\n\n")
	fdout.write("@RELATION directive_keywords\n\n")

	fdout.write("@ATTRIBUTE id NUMERIC\n")
	for elem in patterns:
		inicio = elem.find("b")+1
		fin = elem.find("\\", inicio)
		word = elem[inicio:fin]
		fdout.write("@ATTRIBUTE "+word+" NUMERIC\n")
	fdout.write("@ATTRIBUTE is_directive {TRUE, FALSE}\n")
	fdout.write("\n@DATA\n")

	
	with open(fileIn_name) as fdin:
		csvDictReader = csv.DictReader(fdin)

		i=0
		for line in fdin:
			if i==0:
				i+=1
				continue#skip 1st line

			if i%5000==0:
				print(str(i)+" lines scanned")
			
			row = line.split(',', num_of_columns-1)

			p = re.compile(r'\d+')
			if p.search(row[0]) == None:
				debug.log('wrong id format in line '+str(i+1)+'\n')
			else:
				if not sparce:
					fdout.write(row[0]+"," + ",".join(str(num) for num in getPatternCountList(str(row[num_of_columns-1]), patterns)) +","  +str(row[2])+  "\n")
				else:
					fdout.write("{0 "+row[0]+","  +  ",".join(words for words in getPatternCountListSparse(str(row[num_of_columns-1]), patterns))  +str(len(patterns)+2-1)+" "+str(row[2]) + "}\n")


			i+=1
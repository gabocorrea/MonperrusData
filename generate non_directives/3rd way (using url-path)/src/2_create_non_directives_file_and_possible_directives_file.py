import re

fdout = open("../out/possible_directives_(comments_with_keywords).csv","w")
fdout2 = open("../out/dataset_withID_with_non_directives.csv","w")


patternsStr = r"\bcall\w*\b" + r"|" + r"\binvo\w*\b" + r"|" + r"\bbefore\b" + r"|" + r"\bafter\b" + r"|" + r"\bbetween\b" + r"|" + r"\bonce\b" + r"|" + r"\bprior\b" + r"|" + r"\bmust\b" + r"|" + r"\bmandat\w*\b" + r"|" + r"\brequire\w*\b" + r"|" + r"\bshall\b" + r"|" + r"\bshould\b" + r"|" + r"\bencourage\w*\b" + r"|" + r"\brecommend\w*\b" + r"|" + r"\bmay\b" + r"|" + r"\bassum\w*\b" + r"|" + r"\bonly\b" + r"|" + r"\bdebug\w*\b" + r"|" + r"\brestrict\w*\b" + r"|" + r"\bnever\b" + r"|" + r"\bcondition\w*\b" + r"|" + r"\bstrict\w*\b" + r"|" + r"\bnecessar\w*\b" + r"|" + r"\bportab\w*\b" + r"|" + r"\bstrong\w*\b" + r"|" + r"\bperforman\w*\b" + r"|" + r"\befficien\w*\b" + r"|" + r"\bfast\b" + r"|" + r"\bquick\b" + r"|" + r"\bbetter\b" + r"|" + r"\bbest\b" + r"|" + r"\bconcurren\w*\b" + r"|" + r"\bsynchron\w*\b" + r"|" + r"\block\w*\b" + r"|" + r"\bthread\w*\b" + r"|" + r"\bsimultaneous\w*\b" + r"|" + r"\bdesir\w*\b" + r"|" + r"\balternativ\w*\b" + r"|" + r"\baddition\w*\b" + r"|" + r"\bextend\w*\b" + r"|" + r"\boverrid\w*\b" + r"|" + r"\boverload\w*\b" + r"|" + r"\boverwrit\w*\b" + r"|" + r"\breimplement\w*\b" + r"|" + r"\bsubclass\w*\b" + r"|" + r"\bsuper\w*\b" + r"|" + r"\binherit\w*\b" + r"|" + r"\bwarn\w*\b" + r"|" + r"\baware\w*\b" + r"|" + r"\berror\w*\b" + r"|" + r"\bnote\w*\b"

loops = 0 #put 0 for loop until end (infinite)
myList = []

import csv

list_of_directives_id=[]
with open("../out/directives_withID.csv") as fdDirectives:
	csvDictReader = csv.DictReader(fdDirectives)
	for row in csvDictReader:
		list_of_directives_id.append(row["id"])


p = re.compile(patternsStr, re.IGNORECASE)


fdout.write("id,type,path,text\n")
fdout2.write("id,type,path,text\n")
with open("../data/dataset_withID.csv") as fdDataset:
	i = 0
	for line in fdDataset:
		if i>0:
			if loops<1 and i%500==0:
				print(i)
			if loops>=1 and i>=loops:
				break

			if i not in list_of_directives_id: #!importante! esto asume (correctamente por ahora) que dataset_withID.csv tiene cada ID coincidiendo con el n# de linea
				if p.search(line) == None:
					fdout2.write(line)
				else:
					fdout.write(line)

		i += 1

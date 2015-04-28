import re

fdout = open("../out/dataset_withID_with_phrases_with-IsDirective-Info.csv","w")
fdout.write("id,id_sub,is_directive,type,path,text\n")

patternsStr = r"\bcall\w*\b" + r"|" + r"\binvo\w*\b" + r"|" + r"\bbefore\b" + r"|" + r"\bafter\b" + r"|" + r"\bbetween\b" + r"|" + r"\bonce\b" + r"|" + r"\bprior\b" + r"|" + r"\bmust\b" + r"|" + r"\bmandat\w*\b" + r"|" + r"\brequire\w*\b" + r"|" + r"\bshall\b" + r"|" + r"\bshould\b" + r"|" + r"\bencourage\w*\b" + r"|" + r"\brecommend\w*\b" + r"|" + r"\bmay\b" + r"|" + r"\bassum\w*\b" + r"|" + r"\bonly\b" + r"|" + r"\bdebug\w*\b" + r"|" + r"\brestrict\w*\b" + r"|" + r"\bnever\b" + r"|" + r"\bcondition\w*\b" + r"|" + r"\bstrict\w*\b" + r"|" + r"\bnecessar\w*\b" + r"|" + r"\bportab\w*\b" + r"|" + r"\bstrong\w*\b" + r"|" + r"\bperforman\w*\b" + r"|" + r"\befficien\w*\b" + r"|" + r"\bfast\b" + r"|" + r"\bquick\b" + r"|" + r"\bbetter\b" + r"|" + r"\bbest\b" + r"|" + r"\bconcurren\w*\b" + r"|" + r"\bsynchron\w*\b" + r"|" + r"\block\w*\b" + r"|" + r"\bthread\w*\b" + r"|" + r"\bsimultaneous\w*\b" + r"|" + r"\bdesir\w*\b" + r"|" + r"\balternativ\w*\b" + r"|" + r"\baddition\w*\b" + r"|" + r"\bextend\w*\b" + r"|" + r"\boverrid\w*\b" + r"|" + r"\boverload\w*\b" + r"|" + r"\boverwrit\w*\b" + r"|" + r"\breimplement\w*\b" + r"|" + r"\bsubclass\w*\b" + r"|" + r"\bsuper\w*\b" + r"|" + r"\binherit\w*\b" + r"|" + r"\bwarn\w*\b" + r"|" + r"\baware\w*\b" + r"|" + r"\berror\w*\b" + r"|" + r"\bnote\w*\b"
p = re.compile(patternsStr, re.IGNORECASE)

loops = 0 #put 0 for loop until end (infinite)
myList = []





list_of_directives_id_INT=[]
with open("../out/directives_withID.csv") as fdDirectives:
	i = 1
	for line in fdDirectives:
		if i>1:
			list_of_directives_id_INT.append( int(line.split(",",maxsplit=1)[0]) )
		i+=1



with open("../out/dataset_withID_with_phrases.csv") as fdDataset:
	i = 1
	for line in fdDataset:

		if i>1:
			if loops<1 and i%500==0:
				print(i)
			if loops>=1 and i>=loops:
				break

			line_splitted = line.split(",",maxsplit=5)
			if i>10000 and i%10==0:
				pass
				#print(i)
			if int(line_splitted[0]) not in list_of_directives_id_INT:#no incluimos las lineas que contenian directivas detectadas por Monperrus.
				if p.search(line_splitted[5]) == None:
					fdout.write(','.join([line_splitted[0],line_splitted[1],'0',line_splitted[3],line_splitted[4],line_splitted[5]]))
				else:
					fdout.write(','.join([line_splitted[0],line_splitted[1],'1',line_splitted[3],line_splitted[4],line_splitted[5]]))

		i += 1

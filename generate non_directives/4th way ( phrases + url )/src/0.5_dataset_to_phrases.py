import csv, re
# no se porque, este script produce un output con algunas lineas en blanco entre todas las demas. hay que arreglar esa linea a mano.



################# This can be changed to try other results ############
#regex = r'\.\s+|\.(\\n)+|@param|@return|@deprecated|@exception|@throws|@see|@version|@since|@link|</li>\s*(\\n)*\s*' #|\s*(\\n)*\s*<li>' #TODO: algunas se cortal al ppio, otras al final
################# **************************************** ############
regexEnd = r'\.\s*(&nbsp;)*(<br>)*\s*(&nbsp;)*(\\n)+\s*(&nbsp;)*(<br>)*\s*(&nbsp;)*(\\n)*|\.\s+|</ul>\s*(\\n)*\s*|</ol>\s*(\\n)*\s*'
regexBeg = r'@param|@return|@deprecated|@exception|@throws|@see|@version|@since|@link|@author|<li>'
################# 

fdout = open("../out/dataset_withID_with_phrases.csv","w")
fdout.write("id,id_sub,is_directive,type,path,text\n")

#p = re.compile(regex,re.IGNORECASE)
pEnd = re.compile(regexEnd,re.IGNORECASE)
pBeg = re.compile(regexBeg,re.IGNORECASE)

i=1

with open("../out/dataset_withID (xml2csv output).csv") as fdin_Dataset:
	for line in fdin_Dataset:
		if i>1:
			line_splitted = line.split(",",maxsplit=3)
			row_id = line_splitted[0]
			row_type = line_splitted[1]
			row_path = line_splitted[2]
			row_text = line_splitted[3]

			splitPositionsList = []

			iteratorEnd = pEnd.finditer(row_text)
			for m in iteratorEnd:
				splitPositionsList.append( m.end() )

			iteratorBeg = pBeg.finditer(row_text)
			for m in iteratorBeg:
				splitPositionsList.append( m.start() )

			
			splitPositionsList.sort()

			emptylines=0
			nextStartPos=0
			j=1
			fdout.write(','.join([row_id,str(j-1),'?',row_type,row_path+'#'+str(j-1),row_text])) #todas las frases aca (texto original)
			for pos in splitPositionsList:
				theText = row_text[nextStartPos:pos]
				if len(theText)<=0:
					emptylines+=1
				if len(theText)>=1:
					outstr = ','.join([row_id,str(j),'?',row_type,row_path+'#'+str(j),theText])
					if pos<len(row_text):
						outstr += "\n"
					elif pos>len(row_text):
						print('miError: esto no deberia pasar nunca')
					fdout.write(outstr)
					j+=1
				nextStartPos=pos
				
			theText = row_text[nextStartPos:]
			if nextStartPos<len(row_text) and len(theText)>=1:
				fdout.write(','.join([row_id,str(j),'?',row_type,row_path+'#'+str(j),theText]))

		'''if i>10:
			break'''
		i+=1
	print('miWarning: '+str(emptylines)+' empty PHRASES were ommited')
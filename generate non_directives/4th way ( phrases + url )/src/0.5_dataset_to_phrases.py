import csv, re

################# This can be changed to try other results ############
regex = r'\.\s+|\.(\\n)+|@param|@return|<li>'
################# **************************************** ############

fdout = open("../out/dataset_withID_with_phrases.csv","w")
fdout.write("id,id_sub,is_directive,type,path,text\n")

p = re.compile(regex,re.IGNORECASE)

i=1

with open("../out/dataset_withID (xml2csv output).csv") as fdin_Dataset:
	for line in fdin_Dataset:
		if i>1:
			line_splitted = line.split(",",maxsplit=3)
			row_id = line_splitted[0]
			row_type = line_splitted[1]
			row_path = line_splitted[2]
			row_text = line_splitted[3]


			
			iterator = p.finditer(row_text)
			j=1
			nextStartPos=0
			fdout.write(','.join([row_id,str(j-1),'?',row_type,row_path+'#'+str(j-1),row_text]))
			
			for m in iterator:
				fdout.write(','.join([row_id,str(j),'?',row_type,row_path+'#'+str(j),row_text[nextStartPos:m.start()]]) + "\n")
				nextStartPos = m.end()
				j+=1
				
			fdout.write(','.join([row_id,str(j),'?',row_type,row_path+'#'+str(j),row_text[nextStartPos:]]))
			


		'''if i>10:
			break'''
		i+=1
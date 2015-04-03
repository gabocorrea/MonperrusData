inFileName = "../out/possible_non_directives.csv"
outFileName = inFileName[:-4]+"---readable.csv"


import csv

list_of_apidoc_Text=[]
with open(inFileName) as fdin:
	csvDictReader = csv.DictReader(fdin)
	for row in csvDictReader:
		list_of_apidoc_Text.append(row["apidoc_Text"])



with open(outFileName,"w") as fdout:
	fdout.write("<elem_list>\n")
	for elem in list_of_apidoc_Text:
		print("<elem>", file=fdout)
		print(elem, file=fdout)
		print("</elem>", file=fdout)
	fdout.write("</elem_list>\n")
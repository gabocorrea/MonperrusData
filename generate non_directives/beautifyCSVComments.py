s = " Creates a new help control that provides access to context help.\n <p>\n The <code>TrayDialog</code> implementation of this method creates\n the control, registers it for selection events including selection,\n Note that the parent's layout is assumed to be a <code>GridLayout</code>\n and the number of columns in this layout is incremented. Subclasses may\n override.\n </p>\n \n @param parent the parent composite\n @return the help control\n"


import re

fdin = open("parser-pick_random_lines_without_...-out(maybe_directives).csv")
fdinDataset = open("dataset.csv")
fdout = open("beautifyCSVComments - (out).txt","w")
fdout2 = open("beautifyCSVComments - (out)(original lines).txt","w")
log = open("log.txt","w")

p = re.compile(r"\"")

for line in fdin:
	L=line.split(",",2)

	###log.write("path:\t"+L[1]+"\n")
	###log.write(L[1]+"\n")
	for line02 in fdinDataset:

		###log.write(L[1]+"\n")

		line02_use_this_one = p.sub("", line02)

		###log.write("______________\n"+line02.split(",",2)[1] + "\n" + L[1] +"\n\n\n")
		if (L[1]) in p.sub("", line02.split(",",2)[1]):
			if line02.split(",",2)[2] == "":
				print("asd")
			fdout.write(str(line02.split(",",2)[2]))  ####esto no imprime nada??? wtf  odio este programa. quizas ver otra alternativa para leer los comentarios
			fdout2.write(L[2])
	fdinDataset.seek(0)
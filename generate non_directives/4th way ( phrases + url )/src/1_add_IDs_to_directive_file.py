## Este script se demoró como 50 minutos en terminar !

import csv

fdout_directives_with_id = open("../out/directives_withID.csv","w")
fdout_directives_with_id.write("id,kind,path,text,group_Id\n")

i=0

#leer url's de directive.csv
with open("../data/directive.csv") as fdin_Directives:
	csvObj_directives = csv.DictReader(fdin_Directives)

	with open("../out/dataset_withID (xml2csv output).csv") as fdin_Dataset:
		csvObj_dataset = csv.DictReader(fdin_Dataset)

		for row_directives in csvObj_directives:
			if i%10==0: print(i)
			i+=1

			notfound = True

			for row_dataset in csvObj_dataset:
				#buscarlas en dataset_withID.csv


			#si hay exactamente 1 match en todo el archivo estamos bien, escribimos id en la linea que revisamos de directive.csv
				#si son iguales las url's
				if row_dataset["path"] == row_directives["path"]:
					fdout_directives_with_id.write(str(row_dataset["id"]) + ","+row_directives["kind"]+ ','+row_directives["path"]+ ',"'+row_directives["text"]+ '",'+row_directives["group_Id"]+"\n")
					notfound = False

			if notfound:
				fdout_directives_with_id.write("-1,"+row_directives["kind"]+ ","+row_directives["path"]+ ',"'+row_directives["text"]+ '",'+row_directives["group_Id"]+"\n")


			fdin_Dataset.seek(0)

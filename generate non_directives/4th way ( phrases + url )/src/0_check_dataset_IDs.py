import inspect

i=1
ret = True

with open("../out/dataset_withID (xml2csv output).csv") as fdin_Dataset:

	for line in fdin_Dataset:
		L = line.split(",",maxsplit=1)
		if i>1 and i!=int(L[0]):
			ret = False
			with open("../out/log_"+inspect.getfile(inspect.currentframe()),"w") as fdlog:
				log.write(str(i) + " != " + str(int(L[0])))

		i+=1
		
if ret is True:
	print("no errors found")
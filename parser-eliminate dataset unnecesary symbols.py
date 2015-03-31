import re

fd = open("dataset.csv")
fdout = open("datasetWithNoExtraSymbols-out.csv","w")
i = 0

doOnlyTenLoops = False




lineOut = ""

for line in fd:
	#omitir las ocurrencias de <.*> y de </.*>     :   la sgte regexp sirve     <[^>]*>
	p = re.compile(r"<[^>]*>")
	lineOut = p.sub("", line)

	#omitir los caracteres "
	p = re.compile("\"")
	lineOut = p.sub("", lineOut)

	#omitir los caracteres \n
	p = re.compile(r"\\n")
	lineOut = p.sub("", lineOut)

	#reemplazar todos los espacios dobles, triples o mas por un espacio simple
	p = re.compile(r" {2,}")
	lineOut = p.sub(" ", lineOut)

	fdout.write(lineOut)
	if i > 10 and doOnlyTenLoops:
		break
	i+=1

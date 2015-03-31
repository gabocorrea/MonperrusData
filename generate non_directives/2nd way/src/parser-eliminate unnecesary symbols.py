import re

fd = open("../data/directives_only_the_comments_WithNoExtraSymbols.csv")
fdout = open("../data/directives_only_the_comments_WithNoExtraSymbols_Final.csv","w")
#log = open("../out/log.txt","w")
i = 0

doOnlyTenLoops = False




lineOut = ""

for line in fd:
	#omitir las ocurrencias de <.*> y de </.*>     :   la sgte regexp sirve     <[^>]*>
	#p = re.compile(r"<[^>]*>")
	#lineOut = p.sub("", line)

	#omitir los caracteres "
	p = re.compile("\"")
	lineOut = p.sub("", line)

	#omitir los caracteres \n
	#p = re.compile(r"\\n")
	#lineOut = p.sub("", line)

	#reemplazar todos los espacios dobles, triples o mas por un espacio simple
	p = re.compile(r" {2,}")
	lineOut = p.sub(" ", lineOut)

	fdout.write(lineOut)
	if i > 10 and doOnlyTenLoops:
		break
	i+=1

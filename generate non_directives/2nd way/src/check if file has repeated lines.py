fdin = open("../out/directives_withID.csv")
log = open("../out/log-temp.txt","w")

SetWithTheLinesAlreadyVisited = set()

showError=False

for line in fdin:
	if int(line[:-1]) not in SetWithTheLinesAlreadyVisited:
		SetWithTheLinesAlreadyVisited.add(int(line[:-1]))
	else:
		showError=True
		break

if showError:
	log.write("\n\n*Error*:\nA line was being repeated")
else:
	log.write("done! no line numbers were repeated.")
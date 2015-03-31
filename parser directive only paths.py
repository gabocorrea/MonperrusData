fd = open("directive only paths.csv")
fdout = open("out.txt","w")
i = 0

doOnlyTenLoops = False

fdout.write("filePath,className,methodName\n")
for line in fd:
	filePath = ""
	className = ""
	methodName = ""
	s = ""

	array = line.split("/")
	arrayLength = len(array)
	print(len(array))

	count = 0
	for word in array:
		s += word + "\t"
		if count <= arrayLength-3:
			filePath += word + "/"
		
		if count == arrayLength-3:
			className = word
		elif count == arrayLength-2:
			methodName = word
		count += 1
	filePath = filePath[0:len(filePath)-1]
	fdout.write(filePath+",")
	fdout.write(className+",")
	fdout.write(methodName+"\n")
	if i > 10 and doOnlyTenLoops:
		break
	i+=1
fdout.write("\n\n\n\n\n")

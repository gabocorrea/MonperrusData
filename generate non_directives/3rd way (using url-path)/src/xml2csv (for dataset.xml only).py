
with open ('../out/dataset_withID (xml2csv output).csv','w') as fdout:
	with open('../data/dataset.xml') as fdin:
		fdout.write('id,type,path,text\n')

		counter = 2

		inside = False
		tipo = url = text = None
		i = j = None
		inside_inside = False
		ii = jj = None
		for line in fdin:

			if not inside and '<apidoc' in line:
				inside = True
				text = '"'
				i = line.find('=')
				j = line.find('"', i+2)
				tipo = line[i+2:j]
				i = line.find('=',j)
				j = line.find('"',i+2)
				url = line[i+2:j]
				fdout.write(str(counter)+','+tipo+','+url)
			elif inside and '</apidoc>' in line:
				inside = False
			elif inside and '<![CDATA[' in line and ']]>\n' not in line:
				inside_inside = True
				ii = line.find('<![CDATA[')
				ii = ii + 9
				text += line[ii:]
			elif inside and '<![CDATA[' not in line and ']]>\n' in line:
				inside_inside = False
				jj = line.find(']]>\n')
				text += line[:jj]
				text = text.replace('\n', '\\n')
				fdout.write(','+text+'"\n')
				counter += 1
			elif inside_inside:
				text += line
			elif inside and '<![CDATA[' in line and ']]>\n' in line:
				inside_inside = False
				ii = line.find('<![CDATA[')
				ii = ii + 9
				jj = line.find(']]>\n',ii)
				text += line[ii:jj]
				text = text.replace('\n', '\\n')
				fdout.write(','+text+'"\n')
				counter += 1
			else:
				pass

			if counter%5000==0: print(str(int(counter/20000*100))+'%')

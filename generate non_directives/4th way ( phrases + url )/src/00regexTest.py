import re

regexStart = r'\.\s+|\.(\\n)+|</li>\s*(\\n)*\s*'
regexEnd = r'@param|@return|\s*(\\n)*\s*<li>'

p = re.compile(regexStart, re.IGNORECASE)

input_text = '42,0,1,package,org/apache/commons/collections/list#0,\n<p>\nThis package contains implementations of the\n{@link java.util.List List} interface.\n</p>\n<p>\nThe following implementations are provided in the package:\n<ul>\n<li>TreeList - a list that is optimised for insertions and removals at any index in the list</li>\n<li>CursorableLinkedList - a list that can be modified while the listIterator (cursor) is being used</li>\n<li>NodeCachingLinkedList - a linked list that caches the storage nodes for a performance gain</li>\n</ul>\n</p>\n<p>\nThe following decorators are provided in the package:\n<ul>\n<li>Synchronized - synchronizes method access for multi-threaded environments</li>\n<li>Unmodifiable - ensures the collection cannot be altered</li>\n<li>Predicated - ensures that only elements that are valid according to a predicate can be added</li>\n<li>Typed - ensures that only elements that are of a specific type can be added</li>\n<li>Transformed - transforms each element added</li>\n<li>FixedSize - ensures that the size of the list cannot change</li>\n<li>Lazy - creates objects in the list on demand</li>\n<li>Growth - grows the list instead of erroring when set/add used with index beyond the list size</li>\n<li>SetUnique - a list that avoids duplicate entries like a Set</li>\n</ul>\n</p>\n'

iterator = p.finditer(input_text)

for e in iterator:
	#print(e)
	pass

pos=0
acc=pos
while pos < len(input_text):
	m = re.search(regexStart, input_text[pos:])
	m2 = re.search(regexEnd, input_text[pos:])
	m3 = re.search(r'!!!!!!!!!!!', input_text)
	m4 = re.search(r'ttttttttttt', input_text)
	if m or m2:
		if m and not m2:
			pos += m.start()+1
		elif not m and m2:
			pos += m2.start()+1
		elif m and m2:
			themin = min([m.start(),m2.start()])
			pos+=themin+1
		acc+=pos
		print(pos+)
		
		pass
	else:
		print('else')
		break
	#pos = m.end()
	#print(str(pos)+' '+str(m) + ' ' + input_text[pos:pos+12] + ' ' + str(m.end()))
		
	


'''
for m in iterator:
	print(type(m.re))
	break'''
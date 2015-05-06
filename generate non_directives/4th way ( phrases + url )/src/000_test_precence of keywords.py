from collections import defaultdict
from re import compile

filename='../dataset_withID_without_directives_(only comments).csv'

inputFileName = filename
outputFileName = filename+'__out_txt'

l=compile(r"(\b[a-zA-Z]{3,}\b)").findall(open(inputFileName,'r').read().lower())
f=open(outputFileName,'w')

d = defaultdict(int)
for word in l:
    d[word] += 1

d_copy=dict(d)
alist = []

i=0
while len(d)>0:
	amax=0
	key_index=None
	for key in d.keys():
		if d[key]>amax:
			amax=d[key]
			key_index=key
	alist.append(key_index)
	d.pop(key_index)
	if i%500==0:
		print(i)
	i+=1


col_width = max(len(word) for word in alist) + 2 #padding

for word in alist:
	f.write(word.ljust(col_width) + str(d_copy[word]) + '\n')

f.close()



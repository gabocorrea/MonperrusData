
with open("out_test_size_of_cookie.csv","w") as fd:
	for i in range(12000):
		fd.write(str(i)+",1\n")
		
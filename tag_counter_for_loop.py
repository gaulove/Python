tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for i in tokens:
	if((i[0] is "<" and i[-1] is ">")):
		count =count+1


print(count)
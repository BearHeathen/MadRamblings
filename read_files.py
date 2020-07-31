file = open('file.txt', 'r')

f = file.readlines()

readingList = []
for line in f:
	readingList.append(line.strip())
print(readingList)

file.close()

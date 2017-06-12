df = {}
j = 0
#implement here

#open, read the file, and then close it
file = open('tweet_features.txt', 'r')
while 1:

	line = file.readline()
	if not line:
		break
	list1 = line[:-1].split(' ')
	df[j] = tuple(list1)
	j += 1
#df[i] is a two-element tuple containing the two features.

for i in range(100):
    print(df.get(i,"None"))

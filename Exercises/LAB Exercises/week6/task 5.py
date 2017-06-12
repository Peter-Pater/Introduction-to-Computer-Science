def fastest(list1):
	list1.sort()
	fastest = []
	lowest = []
	time = 0
	fastest.append(min(list1))
	list1.remove(min(list1))
	fastest.append(min(list1))
	list1.remove(min(list1))
	while len(list1) != 0 and len(list1) != 1:
		lowest.append(max(list1))
		list1.remove(max(list1))
		lowest.append(max(list1))
		list1.remove(max(list1))
		time = time + max(lowest)
		time = time + fastest[0] + 2*fastest[1]
		lowest.remove(lowest[0])
		lowest.remove(lowest[0])

	if len(list1) == 0:
		time = time + fastest[1]

	if len(list1) == 1:
		time = time + list1[0] + sum(fastest)

	print(time)


list1 = [1,2,5,10,20]
fastest(list1)



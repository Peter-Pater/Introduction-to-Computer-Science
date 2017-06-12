def larger_than_n(list1,n):
	list2 = []
	for i in range(len(list1)):
		if list1[i] > n:
			list2.append(list1[i])
	print(list2)
	return

list1 = [1,2,3,4,5]
n = 2
larger_than_n(list1,n)

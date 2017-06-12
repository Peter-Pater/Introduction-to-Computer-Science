while True:
	num = input('please input a binary sequence:')
	result = 0
	list1 = list(num)
	list1.reverse()
	power = 0
	for i in list1:
		result = result + int(i)*(2**power)
		power = power + 1
	print(result)

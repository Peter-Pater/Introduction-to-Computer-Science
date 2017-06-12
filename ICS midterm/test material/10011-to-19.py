while True:
	num = int(input('Please input a number:'))
	result = ''
	while True:
		result = str(num%2) + result
		num = num//2
		if num//2 == 0:
			result = str(num%2) + result
			break

	print(result)

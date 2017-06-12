a = {'odd':'red', 'even':'black'} #1 to 10, 19 to 28
b = {'odd':'black', 'even':'red'} #11 to 18, 29 to 36
n = int(input("Please input a number within the range 0 to 36:"))
if n == 0:
	print('green')
elif (1 <= n <= 10) or (19 <= n <= 28):
	if n % 2 == 0:
		print(a['even'])
	else:
		print(a['odd'])
elif (11 <= n <= 18) or (29 <= n <= 36):
	if n % 2 == 0:
		print(b['even'])
	else:
		print(b['odd'])
else:
        print('Error!The number entered is out of range!')

def analyze(x, num=0, letters=''):
	if len(x) == 1:
		if x[0].isdigit() == True:
			num = num + int(x[0])
			return (num, letters)
		elif x[0].isalpha() == True:
			letters = letters + x[0]
			return (num, letters)
	if x[0].isdigit() == True:
		num = num + int(x[0])
	elif x[0].isalpha() == True:
		letters = letters + x[0]
	return analyze(x[1:], num, letters)


if __name__ == "__main__":
    num = 0
    letters = ''
    x = '1a2b3c'
    print(x + ':', analyze(x, num=0, letters=''))
    x = '4Shang56hai'
    print(x + ':', analyze(x, num=0, letters=''))

def stupid_mutiplication(x, y):
	if x == 1:
		return y
	return stupid_mutiplication(x-1,y) + y

# print(stupid_mutiplication(4,7))

def aesterik(n):
	if n == 0:
		return
	aesterik(n-1)
	print('*' * n)http://mnemstudio.org/ai/path/images/modeling_environment_clip_image002a.gif

def finding_max(sequence):
	if len(sequence) == 1:
		return sequence[0]
	rest_max = finding_max(sequence[1:])
	if sequence[0] < rest_max:
		return rest_max
	else:
		return sequence[0]

def Sum(s):
	if len(s) == 1:
		return s[0]
	return s[0] + Sum(s[1:])

def Sum_stair(n):
	if
	return n + Sum_stair(n - 1)



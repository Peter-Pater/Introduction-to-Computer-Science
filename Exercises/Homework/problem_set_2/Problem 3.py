def falling_distance(t1):
	d = (0.5*9.8)*t1**2
	return d

for t in range(1,11):
	print(falling_distance(t))


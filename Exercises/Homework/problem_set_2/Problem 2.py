def calc_average(list1):
	total = 0.0
	for i in range(5):
		total = total + list1[i]
	return total/5.0

def determine_grade(list1):
	for i in range(5):
		if 90 <= list1[i] <= 100:
			print(list1[i],'\t'+'A')
		elif 80 <= list1[i] <= 89:
			print(list1[i],'\t'+'B')
		elif 70 <= list1[i] <= 79:
			print(list1[i],'\t'+'C')
		elif 60 <= list1[i] <= 69:
			print(list1[i],'\t'+'D')
		elif list1[i] <= 59:
			print(list1[i],'\t'+'F')
	print('\n')
	return

i = 1
list1 = [0,0,0,0,0]
while i <= 5:
	score = int(input('Please input your score:'))
	list1[i-1] = score
	i = i + 1

print('the average of the scores is:',calc_average(list1))
determine_grade(list1)

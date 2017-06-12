string1 = input('Please input a string that conforms to the requirement:')
string2 = string1[::-1]
list1 = []
for i in string2:
	list1.append(i)
	if i.isupper():
		list1.append(' ')
list1.reverse()
list1.remove(list1[0])
print(''.join(list1))

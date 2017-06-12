single_digit_numbers = input('please input:')
length = len(single_digit_numbers)
Sum = 0
i = 0
for i in range(0,length):
	Sum = Sum + int(single_digit_numbers[i])
print(Sum)


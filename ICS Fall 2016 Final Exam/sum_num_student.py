def sum_num(n):
	num = str(n)
	if len(num) == 1:
		return int(num[0])
	return int(num[0]) + sum_num(int(num[1:]))


if __name__ == "__main__":
    print(345, ": ", sum_num('345'))
    print(89, ": ", sum_num('89'))

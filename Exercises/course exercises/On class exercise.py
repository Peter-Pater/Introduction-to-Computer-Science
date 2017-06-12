S_WAIT_FOR_OPRD1 = 1
S_WAIT_FOR_OPRD2 = 2
S_WAIT_FOR_OP = 3
S_DONE = 4
result = 0

OPERATOR_LIST = ['+','-','*','/']

state = S_WAIT_FOR_OPRD1
while state != S_DONE:
	if state == S_WAIT_FOR_OPRD1:
		the_input = input('Please input oprand1:')
		if the_input == 'q':
			print('quiting')
			state = S_DONE
		elif the_input == 'c':
			print('cleared')
			state = S_WAIT_FOR_OPRD1
		else:
			if the_input.isdigit():
				state = S_WAIT_FOR_OPRD2
				op1 = int(the_input)
			else:
				state = S_WAIT_FOR_OPRD1

	elif state == S_WAIT_FOR_OPRD2:
		the_input = input('Please input oprand2:')

		if the_input == 'q':
			print('quiting')
			state = S_DONE
		elif the_input == 'c':
			print('cleared')
			state = S_WAIT_FOR_OPRD1
		else:
			if the_input.isdigit():
				state = S_WAIT_FOR_OP
				op2 = int(the_input)
			else:
				state = S_WAIT_FOR_OPRD2

	elif state == S_WAIT_FOR_OP:
		c = input('Please input operator:')

		if the_input == 'q':
			print('quiting')
			state = S_DONE
		elif the_input == 'c':
			print('cleared')
			state = S_WAIT_FOR_OPRD1
		else:
			if c in OPERATOR_LIST:
				if c == '+':
					result = op1 + op2
				elif c == '-':
					result = op1 - op2
				elif c == '*':
					result = op1 * op2
				elif c == '/':
					result = op1/op2
				print(result)
				state = S_WAIT_FOR_OPRD1
			else:
				state = S_WAIT_FOR_OP



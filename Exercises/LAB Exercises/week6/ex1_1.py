from ex1 import*

def main():
	employee[ID_number] = add_new_employee()

def look_up_employee():
	input('please enter ID_number',ID_number)
	if ID_number in list(employee.keys()):
		return employee[ID_number]
	else
		return 'the employee doesn\'t exist'

def add_new_employee():
	name = input('please enter name:')
	ID_number = input('please enter ID number')
	department = input('please enter Department')
	job_title = input('please enter Job title')
	return Employee(name, ID_number, department, job_title)







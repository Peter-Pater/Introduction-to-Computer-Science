class Employee:
	def __init__(self, name, ID_number, department, job_title):
		self.name = name
		self.ID_number = ID_number
		self.department = department
		self.job_title = job_title

	def get_information(self):
		print('name of employee:', self.name)
		print('ID_number of employee:', self.ID_number)
		print('the department the employee is in:', self.department)
		print('the job title of the employee:', self.job_title)
		return

	def get_name(self):
		print('name of employee:', self.name)
		return

	def get_ID_number():
		print('ID_number of employee:', self.ID_number)
		return

	def get_department():
		print('the department the employee is in:',self.department)
		return

	def get_job_title():
		print('the job title of the employee:', self.job_title)
		return

	def set_name(self, name):
		self.name = name

	def set_ID_number(self, ID_number):
		self.ID_number = ID_number

	def set_department(self, department):
		self.department = department

	def set_job_title(self, department):
		self.department = job_title




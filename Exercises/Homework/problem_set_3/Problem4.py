Accounts = open('charge_accounts.txt')
list_accounts = (Accounts.read()).split('\n')
Accounts.close()
account_entered = input('Please enter an account number:')
if account_entered in list_accounts:
	print('The account number you entered is valid')
else:
	print('The account number you entered is invalid')


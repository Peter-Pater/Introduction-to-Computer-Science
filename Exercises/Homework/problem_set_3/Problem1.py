file_boys = open('BoyNames.txt','r')
file_girls = open('GirlNames.txt','r')
list_boys = (file_boys.read()).split('\n')
list_grils = (file_girls.read()).split('\n')
file_boys.close()
file_girls.close()
girl_name = ''
boy_name = ''
while (girl_name == '' and boy_name == ''):
	girl_name = input('please enter a girl\' name:')
	boy_name = input('please enter a boy\'s name:')
if girl_name != '':
	if girl_name in list_grils:
		print('The girl\'s name you entered is among the most popular girl\'s names!')
	else:
		print('The girl\'s name you entered is not among the most popular girl\'s names...')
if boy_name != '':
	if boy_name in list_boys:
		print('The boy\'s name you entered is among the most popular boy\'s names!')
	else:
		print('The boy\'s name you entered is not among the most popular boy\'s names...')


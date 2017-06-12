second = int(input('Please input the seconds:'))
time = {'days':0,'hours':0,'minutes':0,'seconds':0}
if second < 60:
	time['days'] = 0
	time['hours'] = 0
	time['minutes'] = 0
	time['seconds'] = second
elif 60 <= second < 3600:
	time['days'] = 0
	time['hours'] = 0
	time['minutes'] = second//60
	time['seconds'] = second%60
elif 3600 <= second < 86400:
	time['days'] = 0
	time['hours'] = second//3600
	time['minutes'] = second//60 - time['hours'] * 60
	time['seconds'] = second%60
elif 86400 <= second:
	time['days'] = second//86400
	time['hours'] = second//3600 - time['days'] * 24
	time['minutes'] = second//60 - time['days'] * 24 * 60 - time['hours'] * 60
	time['seconds'] = second%60
print(time['days'],':',time['hours'],':',time['minutes'],':',time['seconds'])

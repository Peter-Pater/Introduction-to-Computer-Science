teams = open('WorldSeriesWinners.txt','r')
#print(teams.read())
team_list = (teams.read()).split('\n')
teams.close()
team_entered = input('Please input a team\'s name:')
count = 0
for team in team_list:
	if team_entered == team:
		count += 1
print('The number of the times the team wins the world series is',count)

file_population = open('USPopulation.txt','r')
list_population = (file_population.read()).split('\n')
file_population.close()
# print(list_population)
list_annualChange = []
total = 0
for i in range(len(list_population)-1):
	list_annualChange.append(int(list_population[i+1])-int(list_population[i]))
	total = total + list_annualChange[i]
average = total/(len(list_population)-1)
max_change_year = 1951 + list_annualChange.index(max(list_annualChange))
min_change_year = 1951 + list_annualChange.index(min(list_annualChange))
print('The average annual change in population is',average)
print('The year with the greatest increase in population is',max_change_year)
print('The year with the smallest increase in population is',min_change_year)



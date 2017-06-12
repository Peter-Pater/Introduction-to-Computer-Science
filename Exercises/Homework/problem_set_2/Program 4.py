string1 = input('Please input the string')

# def vowel_consonant(string):
# 	string.lower()
# 	vowel = 0
# 	list1 = ['a','e','i','o','u']
# 	for i in range(5):
# 		for j in range(len(string)):
# 			if list1[i] == string[j]:
# 				vowel = vowel + 1
# 	return vowel

# print('vowel:',vowel_consonant(string1))
# print('consonant:',len(string1)-vowel_consonant(string1))

len([s for s in string1 if s in vowel])

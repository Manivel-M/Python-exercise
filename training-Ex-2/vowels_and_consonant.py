vowels=['a','e','i','o','u']
user_input=raw_input("Enter the string :")
for count_1 in user_input:
	if count_1 in vowels:
		print ('vowel',count_1)
	else:
		print('consonant',count_1)

	

user_input=raw_input("Enter the word :")
vowels=['a','e','i','o','u']
for count_1 in user_input :
	for count_2 in vowels:
		if (count_1==count_2):
		 print "Vowel :",count_1
	else:
		if (count_1!=count_2):
		 print "consonant :",count_1 	
	

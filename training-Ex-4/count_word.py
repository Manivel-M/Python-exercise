
""" Return the number of times that the string "code" appears anywhere in the given string, except
we’ll accept any letter for the d, so "cope" and "cooe" count.
count_code('aaacodebbb') =1
count_code('codexxcode') =2
count_code('cozexxcope') =2 """

def count_word(string):
	count_1 = 0
	string_1 = list(string)
	for count in range(len(string_1)):
		if string_1[count-1] =='c' and string_1[count] == 'o':
			count = count+1
		if string_1[count-3] == 'c' and string_1[count-2] == 'o' and string_1[count] == 'e':
			count_1 = count_1+1
	return count_1

print count_word(raw_input("Enter the word : "))




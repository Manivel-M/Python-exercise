
""" Return the number of times that the string "code" appears anywhere in the given string, except
we will accept any letter for the d, so "cope" and "cooe" count.
Hount_code('aaacodebbb') =1
count_code('codexxcode') =2
count_code('cozexxcope') =2 """

def count_word(string):
	result = 0
	string_1 = list(string)
	for count in range(len(string_1)):
		if string_1[count] == 'c' and string_1[count+1] == 'o' and string_1[count+3] == 'e':
			result = result + 1
	return result

print count_word(raw_input("Enter the word : "))




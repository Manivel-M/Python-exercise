def double_func(stri):
	stri_1 = list(stri)
	for count in range(len(stri_1)):
		stri_1[count] = stri_1[count] * 2
	return ''.join(stri_1)
print double_func(raw_input("Enter the string :"))

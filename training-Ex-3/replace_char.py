"""Write the program to replace the odd position string with X on any strings."""

user_input = raw_input("Enter the string :")
user_list = list(user_input)
for count in range(0,len(user_input)):
	if (count % 2) == 0:
		user_list[count] = 'X'	
print (''.join(user_list))


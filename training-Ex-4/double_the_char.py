"""Given a string, return a string where for every char in the original, there are two chars. Eg.
double_char(The) = TThhee"""

def double_func(user_input):
	usr_copy = list(user_input)
	for count in range(len(usr_copy)):
		usr_copy[count] = usr_copy[count] * 2
	return ''.join(usr_copy)
print double_func(raw_input("Enter the string :"))

"""Given a string, return a string where for every char in the original, there are two chars. Eg.
double_char(The) = TThhee"""

def double_func(user_input):
	new_string = ""
	for char in user_input:
		new_string += char * 2
	return new_string
print double_func(raw_input("Enter the string :"))

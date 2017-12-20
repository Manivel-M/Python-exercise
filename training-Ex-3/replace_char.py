"""Write the program to replace the odd position string with X on any strings."""

user_input = raw_input("Enter the string :")
user_store = []
for count in range(0,len(user_input)):
	user_store.append(user_input[count])
	if (count % 2) == 0:
		user_store[count] = 'X'
	
user_store = ''.join(user_store)	
print user_store


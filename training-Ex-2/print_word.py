"""Print the letters from the word - "gnu-linux is rule the world now'"""

user='gnu-linux is rule the world now'
for letter in user:
	if '-' not in letter and ' ' not in letter:
		print letter
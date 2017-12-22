"""Create the list and add the elements"""

user = []
choice = 'y'
while choice == 'y':
	length = int(raw_input("Enter the length of the list :"))
	for count in range(0,length):
		user.append(raw_input("Enter the input :"))
	print user
	choice = raw_input("Do u need to add elements in list :")
	

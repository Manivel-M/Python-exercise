no = 'n'
yes = 'y'
while 1:
	user_input=raw_input("Enter the input :")
	if user_input == no:	
		print "Loop broke"
		break
	elif user_input == yes:
		print "Loop continue"
		continue
	else:
		print "Invalid input"

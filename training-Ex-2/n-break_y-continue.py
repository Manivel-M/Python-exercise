"""Write the progrum to break the loop if user give n as input, if y continue"""

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

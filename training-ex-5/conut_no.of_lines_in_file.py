"""Write a program to count no of lines in a text file."""

file_op=open(raw_input("Enter the file name with extension :"),"r")
print len(file_op.readlines())
file_op.close()


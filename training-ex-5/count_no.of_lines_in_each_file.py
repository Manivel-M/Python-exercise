"""Write a program to count no of lines in n no of text files and Plot it as a bar graph as File vs Lines."""

import numpy as np
import matplotlib.pyplot as plt

user_input=raw_input("Enter the file name :")
file_co=user_input.split()
no_line_file = [] #Number of lines in a file
#no_file = len(file_co)  #Number of files
for count,name in enumerate(file_co):
	file_op=open(name,"r")
	no_line_file.append(len(file_op.readlines()))
	file_op.close()	


objects = (file_co)
y_pos = np.arange(len(objects))
performance = no_line_file
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of lines')
plt.title('Comparison between number of files and number of lines in files ')
 
plt.show()


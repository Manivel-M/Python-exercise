
"""Read kernel logs and write it to a file with name log-<date>-<time>.log"""

from datetime import datetime

file_op=open("/var/log/kern.log","r")
file_li=["log-",str(datetime.now()),".log"]
file_li_join=''.join(file_li)	
file_cp=open(file_li_join,"w+")
file_store=file_op.readlines()
for count in file_store:
	file_cp.write(count)
file_cp.close()
file_op.close()


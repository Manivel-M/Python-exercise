user_name = raw_input("Enter the name :")
user_store=[]
for i in range(len(user_name),0,-1):
	user_store.append(user_name[i-1])
user_store=''.join(user_store)
print user_store
	

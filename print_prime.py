
for i in range(1,101):
	no=i
	for j in range(2,no):
		if(no%j==0):
			break
	if(no==j):
		print(j)
		

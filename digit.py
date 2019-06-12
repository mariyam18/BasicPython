st=input("Enter string")
d={'alpha':0,'digit':0,'upper':0,'lower':0}
for i in st:
	if(i.isdigit()):
		d['digit']+=1
	elif(i.isalpha()):
		d['alpha']+=1
print(d)
for i in st:
	if(i.isalpha()):
		if(i.isupper()):
			d['upper']+=1
		else:
			d['lower']+=1
print(d)

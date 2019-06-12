fp=open("sk.txt","w")
c=''
while(c!='.'):
	c=input()
	fp.write(c)
fp.close()
fp=open("sk.txt","r")
print(fp.read())


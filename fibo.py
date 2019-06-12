n=int(input("Enter the no :"))

a,b=0,1
print("{}\n{}".format(a,b))
for i in range(2,n+1):
	c=a+b
	print(c)
	a=b
	b=c

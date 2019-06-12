n=int(input("Enter the no.:\n"))

for i in range(2,n):
	if(n%i==0):
		print("Not a prime no.")
		break
if(i==n-1):
	print("prime no.")

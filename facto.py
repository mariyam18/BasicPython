n=int(input("Enter the no.:"))
fact=1
for i in range(1,n+1):
	fact=fact*i
print(fact)
print("factorial of %d is %d \n"%(n,fact))

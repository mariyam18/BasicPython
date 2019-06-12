<<<<<<< HEAD
n=int(input("Enter the no :"))

a,b=0,1
print("{}\n{}".format(a,b))
for i in range(2,n+1):
	c=a+b
	print(c)
	a=b
	b=c
=======
class fib:
	@staticmethod
	def fibo(no):
		a,b=0,1
		print("%d\n%d"%(a,b))
		for i in range(1,no):
			c=a+b
			print(c)
			a,b=b,c
fib.fibo(8)





>>>>>>> 1dd2b0253c40da3b9f83ae138482e640e6682479

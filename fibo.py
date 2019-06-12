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






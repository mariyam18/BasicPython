#summing of list
class Test:
	def add(self,a):
		sum=0
		for i in a:
			sum=sum+i
		print(sum)
b1=Test()
l=[1,2,3,4]
b1.add(l)

# passing class as a object
class Test:
	print("hello")
	@classmethod
	def add(a):
		print("i am here",a)
Test.add()

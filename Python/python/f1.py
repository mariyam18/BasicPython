class Test:
	#def __init__(s):
		#s.foo=[]
	def add(self):
		self.foo=[]   		#when we want self.foo then this statement is excute 
b1=Test()
b2=Test()
b1.add()            #here __init__() function is not there so calling is done
b2.add()  		# here Test.add(b1) can also write
b1.foo.append(2)
b2.foo.append(3)
print(b1.foo)
print(b2.foo)
print(id(b1.foo))
print(id(b2.foo))


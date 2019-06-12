class Test:
	#def __init__(s):
		#s.foo=[]
	def add(a,b):				#at zero position compulsory object is taking   *here a is taking object
		a.foo=[]
		print(b)
b1=Test()
b2=Test()
Test.add(b1,[133,456,'hi','hello'])			#b1.add(argument) OR #Test.add(object,argument)

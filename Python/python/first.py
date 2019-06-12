class Test:
	foo=[]
t1=Test()				#here t1 is object of Test() class
t2=Test()
t1.foo.append(2)			#here we add 2 in list
t2.foo.append(3)
print(t2.foo)
print(t1.foo)
print(id(t1.foo))			#here by id() we locate there address
print(id(t2.foo))



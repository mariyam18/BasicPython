#from __future__ import print_function


for i in range(5,0,-1):
	for j in range(5-i):
		print(end=" ")
	for j in range(i):
		print("*",end=" ")
	print()

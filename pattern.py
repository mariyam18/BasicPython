#from __future__ import print_function


for i in range(5,0,-1):
	for j in range(5-i):
		print(end=" ")
	for j in range(i):
		print("*",end=" ")
	print("")

rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ")  # print number
    # line after each row to display pattern correctly
    print("")

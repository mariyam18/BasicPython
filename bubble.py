li=[]
n=int(input("Enter no of elements")) # taking no of elements
for i in range(n):						# taking elements of list
	elem=int(input("Enter next element"))
	li.append(elem)
for i in range(n-1):
	for j in range(n-1):
		if(li[j]>li[j+1]):
			li[j],li[j+1]=li[j+1],li[j]
print(li)
#sorting algo
#swapping

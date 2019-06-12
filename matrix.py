a=[[0,0,0],[0,0,0],[0,0,0]]
b=[[0,0,0],[0,0,0],[0,0,0]]
c=[[0,0,0],[0,0,0],[0,0,0]]
print("Enter elements of 1st matrix")
for i in range(3):
	for j in range(3):
		a[i][j]=int(input())
print("Enter elements of 2nd matrix")
for i in range(3):
	for j in range(3):
		b[i][j]=int(input())
print("Enter elements of 1st matrix")
for i in range(3):
	for j in range(3):
		c[i][j]=a[i][j]+b[i][j]
print(c)

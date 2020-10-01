lower=int(input("Enter the  1st no.:\n"))
high=int(input("Enter the  2nd no.:\n"))




print("Prime numbers between", lower, "and", high, "are:")

for num in range(lower, high + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

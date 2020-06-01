#import math
def printgp(a, r, i):
	x = pow(r, i)
	print(a * x)
a = int(input("Enter the first term of Geometric series\n"))
r = int(input("Enter the common ratio of Geometric series\n"))
print("The first 10 terms of the series are")
for i in range(0, 10):
	printgp(a, r, i)

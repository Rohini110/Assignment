def countdigit(n):
	count = 0
	while n != 0:
		n //= 10
		count += 1
	return count
def check(n):
	sum = 0
	n3 = n
	n2 = n
	c = countdigit(n)
	while n3 != 0:
		rem = n3 % 10
		sum = sum + int(pow(rem, c))
		n3 = int(n3 / 10)
	if c == 1:
		if n2 == 1:
			print(n2)
	elif n2 == sum:
		print(n2) 		
a = int(input("Enter first number of the range for Armstrong Numbers\n"))
b = int(input("Enter ending number of the range for Armstrong Numbers\n"))
b = b + 1
print("Armstrong numbers in the range are\n")
for n in range(a, b):
		check(n)

	

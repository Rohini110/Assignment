MAX = 100


def lu_decomposition(matrix, n):
	lower = [[0 for x in range(n)]
			 for y in range(n)]
	upper = [[0 for x in range(n)]
			 for y in range(n)]

	for i in range(n):

		# Upper Triangular
		for k in range(i, n):
			sum = 0
			for j in range(i):
				sum += (lower[i][j] * upper[j][k])
			upper[i][k] = matrix[i][k] - sum

		# Lower Triangular
		for k in range(i, n):
			if i == k:
				lower[i][i] = 1  # Diagonal as 1
			else:
				sum = 0
				for j in range(i):
					sum += (lower[k][j] * upper[j][i])
				lower[k][i] = int((matrix[k][i] - sum) / upper[i][i])

	print("The lower triangular matrix is : ")

	for i in range(n):

		# Lower
		for j in range(n):
			print(lower[i][j], end="\t\t")
		print("")

	print("\nThe upper triangular matrix is : ")
	for i in range(n):
		# Upper
		for j in range(n):
			print(upper[i][j], end="\t\t")
		print("")


size = int(input("Enter n(number of rows and columns) : "))
mat = [[0]*size for i in range(0, size)]
m = mat
for i in range(0, size):
	for j in range(0, size):
		m[i][j] = int(input('Enter element [{0}][{1}] : '.format(i+1, j+1)))
print("The entered matrix is : ")
for i in range(0, size):
	for j in range(0, size):
		print(float(m[i][j]), end="\t\t")
	print()
print()

lu_decomposition(mat, size)
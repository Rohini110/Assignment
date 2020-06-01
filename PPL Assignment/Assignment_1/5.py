print("Enter number of page numbers u are going to enter")
n = int(input()) 
lst1 = []
lst2 = []
print("Enter page number list")
for i in range (0, n):
	ele = int(input())
	lst1.append(ele)
for j in range(1, 26):
	if j in lst1:
		continue
	else:
		lst2.append(j)

print("Page numbers not in the list are :\n", lst2)
	

def sum_of_divisor(x):
    sum = 1
    for i in range(2, x):
        if x % i == 0:
            sum += i
    #print(sum)
    return sum



def find_pairs(start, end):
    pairs = []
    for i in range(start, end + 1):
        for j in range(start, end +1):
            x = sum_of_divisor(i)
            y = sum_of_divisor(j)
            if x == j and y == i and i != j and i < j:
                pairs.append((i, j))
                print(str(i) + "and" + str(j) + "is amicable pair")
    return pairs

start = int(input("Enter start of range :"))
end = int(input("Enter end of range :"))
x = []
x = find_pairs(start, end)


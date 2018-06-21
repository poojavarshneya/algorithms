# Count how many BSTs can be created with N nodes

def how_many_BSTs(n):
    if (n <= 1):
        return 1

    sum = 0
    left = 0
    right = 0

    for i in range(1, n+1):
        left = how_many_BSTs(i-1)
        right = how_many_BSTs(n-i)
        sum += left * right

    return sum

#print(how_many_BSTs(1))
print(how_many_BSTs(2))
print(how_many_BSTs(3))
print(how_many_BSTs(4))

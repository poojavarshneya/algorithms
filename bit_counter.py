def count_bits(x):
    num_bits = 0
    while(x):
        print("x = ", x)
        num_bits += x & 1
        print("num_bits = ", num_bits)
        x >>= 1

    return num_bits

count = count_bits("hello")
print(count)
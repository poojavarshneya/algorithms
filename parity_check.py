def parity_check(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

result = parity_check(0b01101)
print (result)

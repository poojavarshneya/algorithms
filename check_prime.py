def isPrime(number):
    remainder = number % 2
    if remainder == 0:
        return 0

    half = int(9 / 2)
    for x in range(3, half + 1):
        if (number % x == 0):
            return 0
    return 1


def detect_primes(a):
    l = len(a)
    result = []
    for x in range(l):
        result.append(isPrime(a[x]))
    return (''.join(map(str, result)))

print(detect_primes([6,2,5,8]))
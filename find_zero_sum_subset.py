def printResult(intArr, start, end):
    print(",".join(map(str, intArr[start: end + 1])))


def sumZero(intArr):
    l = len(intArr)
    result = []

    for i in range(l):
        sum = 0
        for j in range(i, l):
            sum += intArr[j]
            if sum == 0:
                result.append(",".join(map(str, intArr[i: j + 1])))
                break

    return result

print(sumZero([1, 4, -2, -2, 5, -4, 3]))

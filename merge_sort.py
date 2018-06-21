def merge(left, right):
    result = []

    if not left:
        return right
    if not right:
        return left

    l, r = 0, 0
    while (l < len(left) and r < len(right)):
        if (left[l] < right[r]):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    if (l < len(left)):
        result.extend(left[l:])
    if (r < len(right)):
        result.extend(right[r:])

    return result

def merge_sort(array):
    if len(array) < 2:
        return array

    middle = int(len(array) / 2)
    a1 = merge_sort(array[:middle])
    a2 = merge_sort(array[middle:])
    return merge(a1, a2)


print(merge_sort([5,4,3,2,1]))
    # 0,1,2,3,4,5,6
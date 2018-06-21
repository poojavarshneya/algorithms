def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] < array[pivot]:
            begin += 1
            array[i], array[begin] = array[begin], array[i]
            print (array, begin, i)
    array[pivot], array[begin] = array[begin], array[pivot]
    pivot = begin
    print (array, array[pivot])
    return pivot


def quicksort(array, begin = 0, end = None):
    if end is None:
        end = len(array) -1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

def quicksort1(xs):
    if xs:
        pivot = xs[0]
        below = [i for i in xs[1:] if i < pivot]
        above = [i for i in xs[1:] if i >= pivot]
        return quicksort1(below) + [pivot] + quicksort1(above)
    else:
        return xs # empty list

array = [7,6,2,5,8,2,9,4,0]
#quicksort(array)
result = quicksort1(array)
print(result)

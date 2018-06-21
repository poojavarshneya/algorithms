def getMergedIntervals(inputArray):
    results = []
    sortedArray = sorted(inputArray)
    i, j = 0, 1
    while i < len(inputArray):
        new_interval_start = sortedArray[i][0]
        while j < len(inputArray) and sortedArray[i][1] >= sortedArray[j][0]:
            if (sortedArray[j][1] > sortedArray[i][1]):
                i = j
            j = j+1
        new_interval_stop =  sortedArray[i][1]
        results.append([new_interval_start, new_interval_stop])
        i = j
    return results

r = getMergedIntervals([[1,5],[7,11],[2,9],[51,51],[47,50]])

print(r)
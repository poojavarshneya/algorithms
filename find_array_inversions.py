# Author: Pooja Varshneya
# This code counts the total number of array inversions

import unittest

def merge(left, right, count):
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
            count = count + (len(left) - l)
            result.append(right[r])
            r += 1

    if (l < len(left)):
        result.extend(left[l:])
    if (r < len(right)):
        result.extend(right[r:])

    return count, result

def merge_sort_inversion(array, count):
    if len(array) < 2:
        return count, array
    middle = int(len(array) / 2)
    count1, a1 = merge_sort_inversion(array[:middle], count)
    count2, a2 = merge_sort_inversion(array[middle:], count)
    count += count1 + count2
    return merge(a1, a2, count)

def find_array_inversions(array):
    num, result = merge_sort_inversion(array, 0)
    return num

class Tests(unittest.TestCase):
    def test1(self):
        print(self.assertEqual(find_array_inversions([5,4,7,8,3]), 5))

    def test2(self):
        print(self.assertEqual(find_array_inversions([10,9,8,7,6,5]), 15))

    def test3(self):
        print(self.assertEqual(find_array_inversions([10]), 0))

    def test4(self):
        print(self.assertEqual(find_array_inversions([]), 0))

    def test5(self):
        print(self.assertEqual(find_array_inversions([10,1]), 1))

unittest.main()


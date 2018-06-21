def find_maxlen_subseq(array, start, max_len=0, min=0):
    n = len(array)
    if n == 0:
        return 0
    if start == n - 1:
        max_len = 1
        min = array[start]
    elif start < 0:
        return max_len
    elif array[start] < array[start + 1]:
        if array[start] < min:
            max_len = max_len + 1
            min = array[start]
    return find_maxlen_subseq(array, start - 1, max_len, min)


def main_find_maxlen_subseq(array):
    return find_maxlen_subseq(array, len(array) - 1)

print(main_find_maxlen_subseq([-7,10,9,2,3,8,8,1]))
print(main_find_maxlen_subseq([0,1,2,3,4,5]))
print(main_find_maxlen_subseq([1,5,7,8,9]))
print(main_find_maxlen_subseq([10,9,2,5,3,7,101,18]))
print(main_find_maxlen_subseq([4,10,4,3,8,9]))
print(main_find_maxlen_subseq([1,3,6,7,9,4,10,5,6])) #6

#Alternate dp solution: Complexity: Time = O(n^2) and space = O(n)
#import sys

# public class Solution {
#     public int lengthOfLIS(int[] nums) {
#         if (nums.length == 0) {
#             return 0;
#         }
#         int[] dp = new int[nums.length];
#         dp[0] = 1;
#         int maxans = 1;
#         for (int i = 1; i < dp.length; i++) {
#             int maxval = 0;
#             for (int j = 0; j < i; j++) {
#                 if (nums[i] > nums[j]) {
#                     maxval = Math.max(maxval, dp[j]);
#                 }
#             }
#             dp[i] = maxval + 1;
#             maxans = Math.max(maxans, dp[i]);
#         }
#         return maxans;
#     }
# }
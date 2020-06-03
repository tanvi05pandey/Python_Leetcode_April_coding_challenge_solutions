# Given an array of integers and an integer k, you need to find the total number of continuous
# subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
from collections import defaultdict
def subarraySum(nums,k):
    count = 0
    d = defaultdict(int)
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        if s == k:
            count += 1
        if s-k in d:
            count += d[s-k]
        d[s] += 1
    return count

print(subarraySum([3,4,7,2,-3,1,4,2], 7))

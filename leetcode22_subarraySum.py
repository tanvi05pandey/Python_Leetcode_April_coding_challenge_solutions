# Given an array of integers and an integer k, you need to find the total number of continuous
# subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
from collections import defaultdict
def subarraySum(nums,k):
    count = 0
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if sum(nums[i:j+1]) == k:
    #             print(nums[i:j+1])
    #             count+=1
    # return count

    # cummulative_sum = [0]*(len(nums)+1)
    # for i in range(1,len(nums)+1):
    #     cummulative_sum[i] = cummulative_sum[i - 1] + nums[i - 1]
    # print(cummulative_sum)
    # for start in range(len(nums)):
    #     for end in range(1,len(nums)+1):
    #         if cummulative_sum[end] - cummulative_sum[start] == k:
    #             count+=1
    # return count

    # for i in range(len(nums)):
    #     s = 0
    #     for j in range(i,len(nums)):
    #         s+=nums[j]
    #         print(s)
    #         if s == k:
    #             count+=1
    # return count

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

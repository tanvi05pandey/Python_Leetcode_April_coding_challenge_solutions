# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum.
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#[1,2,3,4]
def maxSubArray(nums):
    first = nums[0]
    max_sum = nums[0]
    for i in range(1,len(nums)):
        first = max(first+nums[i], nums[i])
        max_sum = max(first, max_sum)
    return max_sum


#print(maxSubArray([-1,0,-2]))
#print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1,2,-1,-2,2,1,-2,1]))
#print(maxSubArray([-1,-2]))

#print(maxSubArray([-1,-2]))
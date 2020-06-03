# Given an array nums of n integers where n > 1,  return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

def productExceptSelf(nums):
    answer = [1]*len(nums)
    answer[0] = 1
    for i in range(1,len(nums)):
        answer[i] = answer[i-1]*nums[i-1]
    rightproduct = 1
    for i in range(len(nums)-1, -1, -1):
        answer[i] = answer[i]*rightproduct
        rightproduct *= nums[i]
    return answer


print(productExceptSelf([1,2,3,4]))
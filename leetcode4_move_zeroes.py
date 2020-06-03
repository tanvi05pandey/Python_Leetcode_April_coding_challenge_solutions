# Given an array nums, write a function to move all 0s
# to the end of it while maintaining the relative order of the non-zero elements.
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
def moveZeroes(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count+=1
    while count < len(nums):
        nums[count] = 0
        count+=1
    return nums


print(moveZeroes([0,1,0,3,12]))

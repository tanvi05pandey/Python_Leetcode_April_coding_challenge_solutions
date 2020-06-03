# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4


def search(nums, target):
    beg = 0
    end = len(nums)-1
    while beg <= end:
        mid = beg + int((end-beg)/2)
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[beg]:
            if nums[beg] <= target < nums[mid]:
                end = mid-1
            else:
                beg = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                beg = mid+1
            else:
                end = mid-1
    return -1


print(search([4,5,6,7,0,1,2], 0))
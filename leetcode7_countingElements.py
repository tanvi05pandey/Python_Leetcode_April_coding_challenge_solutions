# Given an integer array arr, count element x such that x + 1 is also in arr.
#
# If there're duplicates in arr, count them seperately.
#
# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

def countElements(arr):
    l = len(arr)
    i = 0
    count=0
    while i < l:
        if arr[i]+1 in arr:
            count += 1
        i+=1
    return count


print(countElements([1,1,3,3,5,5,7,7]))
# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:
#
# direction can be 0 (for left shift) or 1 (for right shift).
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.

# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation:
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"

def stringShift(s, shift):
    tot = 0
    for item in shift:
        if item[0] == 0:
            tot-=item[1]
        else: tot+=item[1]
    val = tot%len(s)
    if val < 0: #Left Rotation
        return s[val:] + s[0:val]
    elif val > 0: #Right rotation
        return s[len(s)-val:] + s[0:len(s)-val]
    else: return s


print(stringShift('abcdefg', [[1,1],[1,1],[0,2],[1,3]]))


#print(stringShift('xqgwkiqpif', [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]))
#print(stringShift("wpdhhcj", [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]))


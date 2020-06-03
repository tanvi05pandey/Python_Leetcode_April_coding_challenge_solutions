# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4

def maximalSquare(matrix):
    if not matrix:
        return 0
    r = len(matrix)
    c = len(matrix[0])
    result = [[0 for _ in range(c+1)] for __ in range(r+1)]
    sqlen = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '1':
                result[i][j] = min(result[i-1][j], result[i][j-1], result[i-1][j-1]) + 1
            else:
                result[i][j] = 0
            sqlen = max(sqlen, result[i][j])
    return sqlen * sqlen

# print(maximalSquare(
#     [
#         ['1', '0', '1', '0', '0'],
#         ['1', '0', '1', '1', '1'],
#         ['1', '1', '1', '1', '1'],
#         ['1', '0', '0', '1', '0']
#     ]
# ))

# print(maximalSquare(
#     [["1","1","1","1"],
#      ["1","1","1","1"],
#      ["1","1","1","1"]]
# ))

print(maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]]))
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which
# minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#     [1,3,1],
#     [1,5,1],
#     [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

def minPathSum(grid):
    if len(grid) == 0 or grid is None:
        return 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if i==0 and j==0: # We just want to skip the top-left corner of the grid
                continue
            #for top row
            if i-1 < 0:
                grid[0][j] = grid[0][j] + grid[0][j-1]
            #for leftmost column
            elif j-1 < 0:
                grid[i][0] = grid[i][0] + grid[i-1][0]
            #remaining grid
            else:
                grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])
    return grid[rows-1][cols-1]

print(minPathSum([
    [1,3,1],
    [1,5,1],
    [4,2,1]
]))
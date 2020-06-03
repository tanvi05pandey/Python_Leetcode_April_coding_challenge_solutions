# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
# and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are
# all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1

def numIslands(grid):
    islands = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                mark(grid, r, c)
    return islands

def mark(grid, row, col):
    grid[row][col] = '-'
    #up
    if row > 0 and grid[row-1][col] == '1':
        mark(grid, row-1, col)
    #down
    if row < len(grid)-1 and grid[row+1][col] == '1':
        mark(grid, row+1, col)
    #left
    if col > 0 and grid[row][col-1] == '1':
        mark(grid, row, col-1)
    #right
    if col < len(grid[0])-1 and grid[row][col+1] == '1':
        mark(grid, row, col+1)


# print(numIslands([["1","1","1","1","0"],
#                   ["1","1","0","1","0"],
#                   ["1","1","0","0","0"],
#                   ["0","0","0","0","0"]]))

print(numIslands([['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']]))

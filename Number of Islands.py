'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += self.visit(i,j,grid)
                    
        return islands

    def visit(self,i,j,grid):

        if grid[i][j] != '1':
            return 0

        grid[i][j] = '-1'

        up = i-1 < 0 or (i-1>=0 and grid[i-1][j] in ['0','-1'])
        down = i+1 >= len(grid) or (i+1 < len(grid) and grid[i+1][j] in ['0','-1'])
        left = j-1 < 0 or (j-1>=0 and grid[i][j-1] in ['0','-1'])
        right = j+1 >= len(grid[0]) or (j+1 < len(grid[0]) and grid[i][j+1] in ['0','-1'])

        if up and down and left and right:
            return 1

        up = False
        down = False
        left = False
        right = False

        if i-1>=0 and grid[i-1][j] == '1':
            up = self.visit(i-1,j,grid)
        if i+1 < len(grid) and grid[i+1][j] == '1':
            down = self.visit(i+1,j,grid)
        if j-1>=0 and grid[i][j-1] == '1':
            left = self.visit(i,j-1,grid)
        if j+1 < len(grid[0]) and grid[i][j+1] == '1':
            right = self.visit(i,j+1,grid)

        if up or down or left or right:
            return 1
        
        return 0

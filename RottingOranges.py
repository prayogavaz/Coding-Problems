'''You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.'''

from copy import deepcopy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        nextGrid = deepcopy(grid)
        R , C = len(grid) , len(grid[0])
        
        
        isAllRotten = True
        for i in range(R):
            for j in range(C):
                 if grid[i][j] == 1:
                        isAllRotten = False
                        break
                        
        if isAllRotten:
            return 0

        for i in range(R):
            
            for j in range(C):
                
                if grid[i][j] == 1:
                    
                    if i > 0 and grid[i-1][j] == 2:
                        nextGrid[i][j] = 2
                    if i < R-1 and grid[i+1][j] == 2:
                        nextGrid[i][j] = 2
                    if j > 0 and grid[i][j-1] == 2:
                        nextGrid[i][j] = 2
                    if j < C-1 and grid[i][j+1] == 2:
                        nextGrid[i][j] = 2
                        
        if nextGrid == grid:
            return -1
        
        timeNeededforNextGrid = self.orangesRotting(nextGrid)
        
        if timeNeededforNextGrid == -1:
            return -1
        
        
        return 1 + timeNeededforNextGrid

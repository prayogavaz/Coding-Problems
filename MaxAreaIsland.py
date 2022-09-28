'''You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = float('-inf')
        R, C = len(grid), len(grid[0])
       
        def dfs(r, c):
            
            area = 0
            
            if grid[r][c] == 1:
                area += 1
                grid[r][c] = -2
                if r >= 1: area += dfs(r-1, c)
                if r+1 < R: area += dfs(r+1, c)
                if c >= 1: area += dfs(r, c-1)
                if c+1 < C: area += dfs(r, c+1)
                    
            return area

        
        
        for i in range(R):
            for j in range(C):
                area = dfs(i,j)
                maxArea = max(area,maxArea)
        
        
        return maxArea

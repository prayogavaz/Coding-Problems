'''There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        paths = [[0 for _ in range(n)] for _ in range(m)]

        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i-1 >= 0:
                    paths[i][j] += paths[i-1][j]
                if j-1 >= 0:
                    paths[i][j] += paths[i][j-1]
                    
        return paths[m-1][n-1]

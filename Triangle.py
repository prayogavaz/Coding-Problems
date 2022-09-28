'''Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        minimumPathSum = [[float('inf') for _ in range(len(triangle))] for _ in range(len(triangle[len(triangle)-1]))]
        
        
        minimumPathSum[0][0] = triangle[0][0]
        for m in range(1,len(triangle)):
            
            for n in range(len(triangle[m])):
                
                if n >= 1:
                    minimumPathSum[m][n] = min(minimumPathSum[m-1][n], minimumPathSum[m-1][n-1]) +triangle[m][n]
                else:
                    minimumPathSum[m][n] = minimumPathSum[m-1][n] +triangle[m][n]
                    
                    
        return min(minimumPathSum[len(triangle)-1])

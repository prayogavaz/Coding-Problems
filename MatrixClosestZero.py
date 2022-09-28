'''Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        R, C = len(mat), len(mat[0])
        
        distance = [[float('inf') for _ in range(C)] for _ in range(R)]
        
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    distance[i][j] = 0
            
        
        for i in range(R):
            for j in range(C):
                
                topNeightbourDistance = float('inf')
                leftNeighbourDistance = float('inf')
                
                if i >= 1:
                    topNeightbourDistance = distance[i-1][j]
                if j >= 1:
                    leftNeighbourDistance = distance[i][j-1]
                    
                distance[i][j] = min(distance[i][j], topNeightbourDistance+1, leftNeighbourDistance+1)
                
        for i in range(R-1,-1,-1):
            for j in range(C-1,-1,-1):
                
                downNeightbourDistance = float('inf')
                rightNeighbourDistance = float('inf')
                
                if i < R-1:
                    downNeightbourDistance = distance[i+1][j]
                if j < C-1:
                    rightNeighbourDistance = distance[i][j+1]
                    
                distance[i][j] = min(distance[i][j], downNeightbourDistance+1, rightNeighbourDistance+1)
                
            
        return distance

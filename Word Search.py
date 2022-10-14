'''Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                exist = self.visit(board,visited,i,j,word)
                if exist:
                    return True

        return False

    def visit(self,board,visited,i,j,word):

        if visited[i][j]:
            return False

        if len(word) == 1:
            if board[i][j] == word[0]:
                return True
            else:
                return False

        if board[i][j] != word[0]:
            return False

        visited[i][j] = True

        up = False
        down = False
        left = False
        right = False

        if i-1>= 0:
            up = self.visit(board,visited,i-1,j,word[1:])
        if i+1 < len(board):
            down = self.visit(board,visited,i+1,j,word[1:])
        if j-1>= 0:
            left = self.visit(board,visited,i,j-1,word[1:])
        if j+1 < len(board[0]):
            right = self.visit(board,visited,i,j+1,word[1:])

        visited[i][j] = False

        return up or down or left or right

     

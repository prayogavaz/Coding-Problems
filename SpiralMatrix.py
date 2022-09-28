'''Given an m x n matrix, return all elements of the matrix in spiral order.'''

class Solution(object):
    def spiralOrder(self, array):
        
        
        startingRow = 0
        startingColoumn = 0
        endingRow = len(array)
        endingColoumn = len(array[0])

        result = []

        while startingRow < endingRow and startingColoumn < endingColoumn:

            for i in range(startingColoumn,endingColoumn):
                result.append(array[startingRow][i])
            startingRow += 1

            for i in range(startingRow,endingRow):
                result.append(array[i][endingColoumn-1])
            endingColoumn -= 1

            if endingRow != startingRow:
                for i in range(endingColoumn-1,startingColoumn-1,-1):
                    result.append(array[endingRow-1][i])
                endingRow -= 1

            if endingColoumn != startingColoumn:
                for i in range(endingRow-1,startingRow-1,-1):
                    result.append(array[i][startingColoumn])
                startingColoumn += 1


        return result


'''

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row. '''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowLeft = 0
        rowRight = len(matrix)-1

        while rowLeft <= rowRight:

            if rowLeft + 1 == rowRight or rowLeft == rowRight:
                if target < matrix[rowLeft][len(matrix[0])-1]:
                    row = rowLeft
                elif target > matrix[rowLeft][len(matrix[0])-1]:
                    row=rowRight
                else:
                    return True
                break
            rowMiddle = int((rowLeft+rowRight)/2)
            if matrix[rowMiddle][0] < target:
                rowLeft = rowMiddle
            elif matrix[rowMiddle][0] > target:
                rowRight = rowMiddle
            else:
                row = rowMiddle
                break


        columnLeft = 0
        columnRight = len(matrix[0])-1

        while columnLeft <= columnRight:

            if columnLeft + 1 == columnRight or columnLeft == columnRight:
                if target == matrix[row][columnLeft] or target == matrix[row][columnRight]:
                    return True
                else:
                    return False

            columnMiddle = int((columnLeft+columnRight)/2)
            if matrix[row][columnMiddle] < target:
                columnLeft = columnMiddle
            elif matrix[row][columnMiddle] > target:
                columnRight = columnMiddle
            else:
                return True

        return False

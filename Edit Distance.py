'''Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        if len(word1) == 0:
            return len(word2)

        if len(word2) == 0:
            return len(word1)

        editDistance = [[float('inf') for _ in range(len(word2))] for _ in range(len(word1))]


        for i in range(len(word1)):
            if word2[0] in word1[:i+1]:
                editDistance[i][0] = i
            else:
                editDistance[i][0] = i+1

        for j in range(len(word2)):
            if word1[0] in word2[:j+1]:
                editDistance[0][j] = j
            else:
                editDistance[0][j] = j+1


        for i in range(1,len(word1)):
            for j in range(1,len(word2)):

                x = editDistance[i-1][j-1]
                y = editDistance[i][j-1]
                z = editDistance[i-1][j]


                if word1[i] == word2[j]:
                    editDistance[i][j] = min(x, y+1, z+1)
                else:
                    editDistance[i][j] = min(x, y, z) + 1

        return editDistance[len(word1)-1][len(word2)-1]

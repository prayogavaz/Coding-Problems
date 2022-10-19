'''Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        if len(text1) == 0 or len(text2) == 0:
            return 0

        lcs = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        for j in range(len(text2)):
            if text1[0] in text2[:j+1]:
                lcs[0][j] = 1
            else:
                lcs[0][j] = 0

        for i in range(len(text1)):
            if text2[0] in text1[:i+1]:
                lcs[i][0] = 1
            else:
                lcs[i][0] = 0


        for i in range(1,len(text1)):
            for j in range(1,len(text2)):

                x = lcs[i-1][j-1]
                y = lcs[i][j-1]
                z = lcs[i-1][j]

                if text1[i] == text2[j]:
                    lcs[i][j] = max(x+1, y, z)
                else:
                    lcs[i][j] = max(x, y, z)

        return lcs[len(text1)-1][len(text2)-1]
      
      
      
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        if len(text1) == 0 or len(text2) == 0:
            return 0

        lcs = [0 for _ in range(len(text2))]

        for j in range(len(text2)):
            if text1[0] in text2[:j+1]:
                lcs[j] = 1
            else:
                lcs[j] = 0

       
        for i in range(1,len(text1)):

            new_lcs = [0 for _ in range(len(text2))]

            if text2[0] in text1[:i+1]:
                new_lcs[0] = 1
            else:
                new_lcs[0] = 0

            for j in range(1,len(text2)):

                x = lcs[j-1]
                y = new_lcs[j-1]
                z = lcs[j]

                if text1[i] == text2[j]:
                    new_lcs[j] = max(x+1, y, z)
                else:
                    new_lcs[j] = max(x, y, z)

            lcs = new_lcs

        return lcs[len(text2)-1]

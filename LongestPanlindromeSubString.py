'''Given a string s, return the longest palindromic substring in s.'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        result = [[0 for _ in range(len(s)+1)] for _ in range(len(s))]
        
        maximumLength = 0
        resulti, resultj = -1,-1
        
     
        for length in range(1,len(s)+1):
            
            for i in range(len(s)):
                
                j = i + length

                if j >= 1 and j < len(s)+1 and s[i] == s[j-1]:
                
                    if i == j-1 or i == j-2:
                        result[i][j] = 1
                    elif result[i+1][j-1]:
                        result[i][j] = 1
                        
                    if result[i][j] and j - i > maximumLength:
                        resulti, resultj = i, j

        return s[resulti:resultj]

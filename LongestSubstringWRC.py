'''Given a string s, find the length of the longest substring without repeating characters.'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        i = 0
        
        longestSubstring = s[0]
        
        while i < len(s):
            
            characters = {}
            characters[s[i]] = i
            
            j = i+1
            
            while j < len(s):
                
                if s[j] in characters.keys():
                    i = characters[s[j]]+1
                    break
                else:
                    if len(longestSubstring) < len(s[i:j+1]):
                        longestSubstring = s[i:j+1]
                    characters[s[j]] = j
                    j = j+1
                    
            if j == len(s):
                break
                
     
        return len(longestSubstring)

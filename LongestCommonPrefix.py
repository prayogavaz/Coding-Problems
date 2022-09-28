'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        
        
        longestPrefix = strs[0]
        
        i = 1
        while i < len(strs) and longestPrefix != '':
            
            if not strs[i].startswith(longestPrefix):
                i = 1
                longestPrefix = longestPrefix[0:len(longestPrefix)-1]
                continue
                
            i += 1
            
                
        return longestPrefix
        

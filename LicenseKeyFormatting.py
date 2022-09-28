'''You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.'''



class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        characters = []
        for i in range(len(s)-1,-1,-1):
            if s[i] != '-':
                characters.append(s[i])
                
        
        firstGroup = len(characters)%k
            
        result = []
        
        for i in range(firstGroup):
            result.append(characters.pop())
            
        
        if firstGroup and len(characters):
            result.append('-')
            
        
        i=0
        while len(characters):
            result.append(characters.pop())
            i += 1
            if i == k and len(characters):
                result.append('-')
                i = 0
                
        return ''.join(result).upper()

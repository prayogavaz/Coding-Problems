'''Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
       
    
        if len(s) <= 1:
            return s
    
        
        for i in range(int(len(s)/2)):
            
            s[i] , s[len(s)-i-1] = s[len(s)-i-1], s[i]

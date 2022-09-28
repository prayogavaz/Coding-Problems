'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.'''

class Solution(object):
    def reverseWords(self, s):
        
        s=list(s)
        
        #self.reverseString(s)
        lastWordStart = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverseString(s,lastWordStart,i-1)
                lastWordStart = i + 1
        
        self.reverseString(s,lastWordStart,len(s)-1)
        
        return ''.join(s)
        
        
    def reverseString(self, s, startIndex = 0, endIndex = -1):
        
        if endIndex == -1:
            endIndex = len(s)-1
            
        if endIndex - startIndex <= 0:
            return s
        
     
        for i in range(startIndex, int((endIndex+startIndex+1)/2)):
            
            s[i] , s[endIndex-i+startIndex] = s[endIndex-i+startIndex], s[i]

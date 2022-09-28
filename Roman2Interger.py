''' Given a roman numeral, convert it to an integer.'''

class Solution:
    
    def romanToInt(self, s: str) -> int:
        
        dict_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return dict_values[s[0]]
                
        
        if s[0] == 'I' and s[1] == 'V':
            return 4 + self.romanToInt(s[2:])
        
        if s[0] == 'I' and s[1] == 'X':
            return 9 + self.romanToInt(s[2:])
        
        if s[0] == 'X' and s[1] == 'L':
            return 40 + self.romanToInt(s[2:])
        
        if s[0] == 'X' and s[1] == 'C':
            return 90 + self.romanToInt(s[2:])
        
        if s[0] == 'C' and s[1] == 'D':
            return 400 + self.romanToInt(s[2:])
        
        if s[0] == 'C' and s[1] == 'M':
            return 900 + self.romanToInt(s[2:])
        
        
        
        return dict_values[s[0]] + self.romanToInt(s[1:])

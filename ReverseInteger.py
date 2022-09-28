'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.'''

class Solution(object):
    def reverse(self, x):
        
        isNegative = False
        
        if x < 0:
            
            isNegative = True
            x *= -1
            
        number = 0
        
        

        while x > 0:
            
            number = (number * 10) + x%10
            x = int(x/10)
            if number > 2147483647:
                return 0
            
        if isNegative:
            number *= -1
            
        return number

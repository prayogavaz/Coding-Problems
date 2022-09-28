'''Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.'''


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        
        if n == 1:
            
            return True
        
        if n%3 == 0:
            
            return self.checkPowersOfThree (n/3)
        
        elif (n-1) % 3 == 0:
            
            return self.checkPowersOfThree ((n-1)/3)
        
        else:
            
            return False

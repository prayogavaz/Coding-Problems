'''Given an integer n, return true if it is a power of two. Otherwise, return false.'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        return not n & n-1

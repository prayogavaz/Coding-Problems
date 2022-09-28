'''Implement pow(x, n), which calculates x raised to the power n (i.e., xn).'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        if n == 0:
            
            return 1
        
        
        if n < 0:
            
            return (1/self.myPow(x,-n))
        
        if n == 1:
            
            return x
        
        if n % 2 == 0:
            
            halfPower = self.myPow(x,n/2)
            
            return halfPower * halfPower
        

        else:
            
            halfPower = self.myPow(x,(n-1)/2)
            
            return halfPower * halfPower * x

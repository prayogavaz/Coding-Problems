'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        result = [0 for _ in range(n+1)]
        
        result[0] = 0
        result[1] = 1
        result[2] = 2
        
        for i in range(3,n+1):
            result[i] = result[i-1] + result[i-2]
            
        return result[n]

'''You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.'''

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        
        result = [[0 for _ in range(max(target,k)+1)] for _ in range(n+1)]

        for j in range(1,k+1):
            result[1][j] = 1


        for i in range(2,n+1):
            for j in range(1,k+1):
                for r in range(1,target+1):
                    if r-j >= 0:
                        result[i][r] += result[i-1][r-j]

        return result[n][target]%((10**9)+7)

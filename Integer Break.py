'''Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.'''

class Solution:
    def integerBreak(self, n: int) -> int:

        results = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1,n+1):

            for j in range(1,i+1):

                if i == j:
                    results[i][j] = 1
                    continue

                if j == 1:
                    results[i][1] = i
                    continue

                for r in range(1,i+1):
                    results[i][j] = max(results[i][j], results[r][j-1]*(i-r))

        return max(results[n][2:])
      
      
      
   class Solution:
    def integerBreak(self, n: int) -> int:

        results = [0 for _ in range(n+1)]
        result = 0
        
        for j in range(1,n+1):

            new_results = [0 for _ in range(n+1)]

            for i in range(1,n+1):

                if 1 == j:
                    new_results[i] = i
                    continue

                if i == j:
                    new_results[i] = 1
                    continue

                for r in range(1,i+1):
                    new_results[i] = max(new_results[i], results[r]*(i-r))

            results = new_results
            if j >= 2:
                result = max(result,max(results))

        return result

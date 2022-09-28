'''Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        if k == 0 or n ==0 :
            return []

        if k == 1:
            return [[x] for x in range(1,n+1)]

        if n == k:
            return [[x for x in range(1, n+1)]]

        combinationsWithn = self.combine(n - 1, k - 1)
        combinationsWithoutn = self.combine(n - 1, k)

        for combination in combinationsWithn:
            combination.append(n)

        combinationsWithn.extend(combinationsWithoutn)
        return combinationsWithn

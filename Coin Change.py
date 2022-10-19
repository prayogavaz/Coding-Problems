'''You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        minCoins = [float('inf') for i in range(amount+1)]
        minCoins[0] = 0

        for i in range(1, amount+1):

            for j in coins:
                if i-j>=0:
                    minCoins[i] = min(minCoins[i], minCoins[i-j]+1) 

        
        if minCoins[amount] == float('inf'):
            return -1

        return minCoins[amount]



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        results = {}
        
        self.coinChangeR(coins, amount,results)

        if results[amount] == float('inf'):
            return -1

        return results[amount]



    def coinChangeR(self, coins: List[int], amount: int, results) -> int:

        if amount == 0:
            results[amount] = 0

        if amount in coins:
            results[amount] = 1

        if amount < 0:
            results[amount] = float('inf')

        if amount in results.keys():
            return results[amount]

        result = float('inf')
        for j in coins:

            result = min(self.coinChangeR(coins, amount-j, results)+1, result)

        results[amount] = result

        return results[amount]

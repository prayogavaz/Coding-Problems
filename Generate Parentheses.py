'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''

class Solution:
    def generateParenthesis(self, n: int, open=0, close=0, s = '', results = []) -> List[str]:

        if open == 0 and close == 0:
            results = []
            
        if close > open:
            return results

        if open == n and close == n:
            results.append(s)

        if open < n:

            self.generateParenthesis(n,open+1, close, s+'(',results)

        if close < n:

            self.generateParenthesis(n,open, close+1, s+')',results)

        return results

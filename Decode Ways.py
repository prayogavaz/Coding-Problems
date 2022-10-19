'''A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.'''

class Solution:
    def numDecodings(self, s: str) -> int:

        valueMap = {}
        for i in range(1,27):
            valueMap[str(i)] = list(string.ascii_uppercase)[i-1]
        

        return self.numDecodingsR(s,valueMap)


    def numDecodingsR(self, s, valueMap, results = {}):

        if len(s) == 0:
            return 1

        if s in results.keys():
            return results[s]

        count = 0
        remainingResult = 0

        if len(s) >= 1 and s[0] in valueMap.keys():
            remainingResult = self.numDecodingsR(s[1:],valueMap,results)
            results[s[1:]] = remainingResult

        count += remainingResult
        remainingResult = 0

        if len(s) >= 2 and s[0:2] in valueMap.keys():
            remainingResult = self.numDecodingsR(s[2:],valueMap,results)
            results[s[2:]] = remainingResult

        count += remainingResult

        results[s] = count

        return results[s]

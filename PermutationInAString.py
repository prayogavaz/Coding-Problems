'''Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.'''

import string

class Solution:
    def checkInclusion(self,s1: str, s2: str) -> bool:
        s1Counts = {}
        s2Counts = {}

        for alphabet in list(string.ascii_lowercase):
            s1Counts[alphabet] = 0
            s2Counts[alphabet] = 0

        for i in range(len(s1)):
            s1Counts[s1[i]] += 1

        for i in range(len(s1)):
            if i >= len(s2):
                return False
            s2Counts[s2[i]] += 1

        if s1Counts == s2Counts:
            return True

        i = len(s1)

        while i < len(s2):
            s2Counts[s2[i - len(s1)]] -= 1
            s2Counts[s2[i]] += 1

            if s1Counts == s2Counts:
                return True

            i += 1

        return False
        

'''Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        results = {}
        wordDictHash = {}

        for word in wordDict:
            wordDictHash[word] = 1

        return self.wordBreakR(s, wordDictHash, results)


    def wordBreakR(self, s, wordDictHash, results) -> bool:

        if len(s) == 0:
            return True

        if s in results.keys():
            return results[s]

        for word in wordDictHash.keys():

            remainingResult = False
            if s[0:len(word)] == word:
                remainingResult = self.wordBreakR(s[len(word):],wordDictHash, results)
                results[s[len(word):]] = remainingResult

            if remainingResult:
                results[s] = True
                return results[s]

        results[s] = False
        return results[s]

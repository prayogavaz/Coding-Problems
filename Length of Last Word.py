'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length = 0
        i = 0
        while i < len(s):

            if s[i] == ' ':
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i == len(s):
                    break
                else:
                    length = 0
            else:
                length += 1
                i += 1

        return length
        

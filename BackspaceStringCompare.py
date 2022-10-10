'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_ = []
        for i in range(len(s)):
            if s[i] != '#':
                s_.append(s[i])
            elif len(s_):
                s_.pop()

        t_ = []
        for i in range(len(t)):
            if t[i] != '#':
                t_.append(t[i])
            elif len(t_):
                t_.pop()

        if ''.join(s_) == ''.join(t_):
            return True

        return False

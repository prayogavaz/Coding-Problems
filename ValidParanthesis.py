'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''


class Solution(object):
    def isValid(self, s):
        
        
        stack = []
        
        for i in range(len(s)):
            
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                continue
                
            if s[i] == '}':
                if len(stack) == 0 or stack[len(stack)-1] != '{':
                    return False
                else:
                    stack.pop()
                    
            if s[i] == ']':
                if len(stack) == 0 or stack[len(stack)-1] != '[':
                    return False
                else:
                    stack.pop()
                    
            if s[i] == ')':
                if len(stack) == 0 or stack[len(stack)-1] != '(':
                    return False
                else:
                    stack.pop()
                    
        if len(stack) != 0:
                return False
            
        return True

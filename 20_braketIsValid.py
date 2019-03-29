class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for ch in s:
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            elif ch == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            elif ch == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            elif ch == '}' or ch == ']' or ch == ')':
                return False
        if len(stack) == 0:
            return True
        else:
            return False
            
            
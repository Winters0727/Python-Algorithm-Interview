class Solution:
    def isValid(self, s: str) -> bool:
        open_list, close_list = ['(', '{', '['], [')', '}', ']']
        stack = list()
        s_list = list(s)
        
        while s_list:
            b = s_list.pop()
            if b in close_list:
                stack.append(b)
            else:
                if not stack or (open_list.index(b) != close_list.index(stack[-1])):
                    return False
                stack.pop()
        if stack:
            return False
        return True
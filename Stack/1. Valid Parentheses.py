class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        bracket_map = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in bracket_map:
                stack += [c]
            elif not stack or bracket_map[stack.pop()] != c:
                    return False
            
        return stack == []

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv',
            '9':'wxyz'}
        
        res = []
        combo = ''
            
        def dfs(i, combo):
            if i == len(digits):
                res.append(combo)
                return
            
            for c in d[digits[i]]:
                dfs(i+1, combo + c)        
            
        if digits:
            dfs(0, '')
        return res

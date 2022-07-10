class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(open_n, closed_n, path):

            if open_n == closed_n == n:
                res.append(path)
                return
            
            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")
            
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")
                
        res = []
        backtrack(0, 0, "")
        return res

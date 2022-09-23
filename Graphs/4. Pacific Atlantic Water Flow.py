class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            if (r in range(ROWS) and
                c in range(COLS) and
                (r, c) not in visit and
                heights[r][c] >= prevHeight):
                visit.add((r, c))
                dfs(r+1, c, visit, heights[r][c])
                dfs(r-1, c, visit, heights[r][c])
                dfs(r, c+1, visit, heights[r][c])
                dfs(r, c-1, visit, heights[r][c])
                
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
            
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
            
        res = []
        for cell in pac:
            if cell in atl:
                res.append(cell)
                
        return res

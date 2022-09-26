class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c):
            if r in range(ROWS) and c in range(COLS) and board[r][c] == 'O':
                board[r][c] = '*'
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
                
        
        # change unsurrounded O to *
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    dfs(r, c)
        
        # change surrounded O to X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                
                
        #change unsurrounded * to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '*':
                    board[r][c] = 'O'

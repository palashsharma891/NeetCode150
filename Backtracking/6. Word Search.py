class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        l = len(word)
        
        def dfs(r, c, pos):
            
            if pos >= l:
                return True
            
            if 0 <= r < ROWS and 0 <= c < COLS and word[pos] == board[r][c]:
                temp = board[r][c]
                board[r][c] = None

                if dfs(r-1, c, pos+1) or dfs(r+1, c, pos+1) or dfs(r, c-1, pos+1) or dfs(r, c+1, pos+1):
                    return True

                board[r][c] = temp
            
            return False
            
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
            
        return False

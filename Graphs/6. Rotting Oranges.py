class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        time = 0
        q = collections.deque()
        fresh = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            qlen = len(q)
            for i in range(qlen):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
                
        return time if not fresh else -1

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        
        def bfs(r, c, area):
            q = [(r, c)]
            visited.add((r, c))
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while q:
                row, col = q.pop(0)
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r, c))
                        area += 1
                        
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c, 1))
                
        return max_area

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = [(r, c)]
            visited.add((r, c))
            
            while q:
                row, col = q.pop(0)
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < rows and
                        0 <= c < cols and
                        grid[r][c] == '1' and
                        (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                    
        return islands

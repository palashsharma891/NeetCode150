class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        visited = set()
        visited.add((0,0))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if neiR in range(N) and neiC in range(N) and (neiR, neiC) not in visited:
                    visited.add((neiR, neiC))
                    heapq.heappush(minHeap, [max(grid[neiR][neiC], t), neiR, neiC])

from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        q = collections.deque()

        def addRoom(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                rooms[r][c] == -1 or
                (r, c) in visited):
                return
            visited.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            qlen = len(q)
            for i in range(qlen):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1

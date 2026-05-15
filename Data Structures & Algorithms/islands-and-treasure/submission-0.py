from typing import List
from typing import Tuple
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        COLUMNS, ROWS = len(grid[0]), len(grid)
        q: deque = deque()
        if grid:
            q.append((grid[0][0], 0, 0))

        def bfsFrom0(cord: Tuple[int, int]):
            bfsQ = deque()
            r, c = cord
            bfsQ.append((grid[r][c], r, c,0))
            visited = {}

            while bfsQ:
                currNodeValFun, r, c,i = bfsQ.popleft()

                grid[r][c] = min(grid[r][c], i) if grid[r][c] != 0 else 0
                visited[(r,c)] = True

                for x, y in directions:
                    newR, newC = r+x, c+y
                    if min(newR, newC) < 0 or newR >= ROWS or newC >= COLUMNS or (newR,newC) in visited or grid[newR][newC] == -1:
                        continue  # don't put through
                    bfsQ.append((grid[newR][newC], newR, newC,i+1))

        # find a 0
        for i in range(ROWS):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfsFrom0((i,j))
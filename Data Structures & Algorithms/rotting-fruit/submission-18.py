from collections import deque
from typing import Tuple
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # WORKS FOR 1 ROTTEN, DIDN'T REALISE THEY'LL BE 2 OR MORE
        # scream bfs
        ROWS,COLS = len(grid),len(grid[0])
        q = deque()
        minutes = 0

        movements = [[1,0],[0,1],[-1,0],[0,-1]]

        def bfs():
            mins=0
            while q:
                for i in range(len(q)):
                    r,c,mins = q.popleft()
                    grid[r][c] = 3

                    for mR,mC in movements:
                        newR,newC = r+mR,c+mC
                        if min(newR,newC) < 0 or newR >= ROWS or newC >= COLS or grid[newR][newC] != 1:
                            continue
                        q.append((newR,newC,mins+1))
            return mins
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 2:
                    q.append((x,y,0))
        minutes = bfs()

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    return -1
        
        return minutes



        
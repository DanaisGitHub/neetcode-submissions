class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS , COLS= m,n
        # mem:dict[tuple,int] = {}
        
        # for x in range(m+1):
        #     for y in range(n+1):
        #         mem[(x,y)] = 0
        
        # mem[(ROWS-1,COLS-1)] = 1

        # # caching / mem
        # def dfsMem (r:int,c:int)->int:
        #     if min(r,c) < 0 or r >= ROWS or c >= COLS:
        #         return 0
            
        #     if (r,c) in mem and mem[(r,c)] != 0:
        #         return mem[(r,c)]
            
        #     mem[(r,c)] = dfsMem(r+1,c) + dfsMem(r,c+1)
            
        #     return mem[(r,c)]
        
        # return dfsMem(0,0)

        ROWS, COLS = m, n
        dpGrid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        
        for row in dpGrid:
            row[COLS-1] = 1

        dpGrid[-1] = [1] * COLS

        for r in range(ROWS-2, -1, -1):
            for c in range(COLS-2, -1, -1):
                dpGrid[r][c] += dpGrid[r+1][c] + dpGrid[r][c+1]

        return dpGrid[0][0]



        






        
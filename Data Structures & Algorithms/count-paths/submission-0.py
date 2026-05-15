class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS , COLS= m,n
        mem:dict[tuple,int] = {}
        
        for x in range(m+1):
            for y in range(n+1):
                mem[(x,y)] = 0
        
        mem[(ROWS-1,COLS-1)] = 1

        # caching / mem
        def dfsMem (r:int,c:int)->int:
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
                return 0
            
            if (r,c) in mem and mem[(r,c)] != 0:
                return mem[(r,c)]
            
            mem[(r,c)] = dfsMem(r+1,c) + dfsMem(r,c+1)
            
            return mem[(r,c)]
        
        return dfsMem(0,0)

        
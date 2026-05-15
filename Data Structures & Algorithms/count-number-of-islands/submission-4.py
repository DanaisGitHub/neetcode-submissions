class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowMax, colMax = len(grid), len(grid[0])
        movements = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        islands = 0

        def dfs(currRow: int, currCol: int) -> None:

            if min(currCol, currRow) < 0 or currCol >= colMax or currRow >= rowMax:
                return
            if grid[currRow][currCol] == '0':
                return

            grid[currRow][currCol] = '0'

            for (ri, ci) in movements:
                dfs(currRow+ri, currCol+ci)

        for r in range(rowMax):
            for c in range(colMax):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        return islands

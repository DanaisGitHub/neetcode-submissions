class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # same as before
        # adhog search through the graph until we find an island
        # once we find an island, dfs find all/only that island
        # as you do add 1 to count, and take max of currCount and maxCount

        maxCount = 0
        rowMax, colMax = len(grid), len(grid[0])
        movements = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(currRow: int, currCol: int, count: int) -> int:
            # base cases
            # out of bounds
            if min(currCol, currRow) < 0 or currCol >= colMax or currRow >= rowMax:
                return 0
            if grid[currRow][currCol] == 0:
                return 0
        
            grid[currRow][currCol] = 0
            print(count)

            for (ri, ci) in movements:
                count = max(count,dfs(currRow+ri, currCol+ci, count+1))
            return count
        
        for r in range(rowMax):
            for c in range(colMax):
                if grid[r][c] == 1:
                    maxCount = max(maxCount,dfs(r, c, 1))

        return maxCount
        
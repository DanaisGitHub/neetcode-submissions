class Solution:
    def climbStairs(self, n: int) -> int:
        # there are 3 ways of solving this
        # recursivly
        # memoization
        # dp

        # recursive

        def dfs(num:int):
            if num ==1 :
                return 1
            if num == 2:
                return 2
            
            return dfs(num-1) + dfs(num-2)
        
        return dfs(n)
        
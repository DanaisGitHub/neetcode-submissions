class Solution:
    def climbStairs(self, n: int) -> int:
        # there are 3 ways of solving this
        # recursivly
        # memoization
        # dp

        # recursive

        def dfs(num:int,memoisation:dict[int,int]):
            if num in memoisation:
                return memoisation[num]
            memoisation[num] = dfs(num-1,memoisation) + dfs(num-2,memoisation)
            
            return  memoisation[num]
        
        return dfs(n,{1:1,2:2})
        
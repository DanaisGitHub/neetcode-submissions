class Solution:
    def climbStairs(self, n: int) -> int:
        # there are 3 ways of solving this
        # recursivly
        # memoization
        # dp

        # recursive

        if n <= 2:
            return n
        
        dp = [0] * (n ) # dp = [0,0,...,0] # why +1 ?

        dp[0], dp[1] = 1, 2
        for i in range(2, n): # why 
            dp[i] = dp[i-2] + dp[i-1]

        return dp[-1]

        
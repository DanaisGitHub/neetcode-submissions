class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        nAdd1 = n+1
        dp = [0] * nAdd1
        for i in range(2, n+1):
            dp[i] += min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])# dp = total cost to get (ne i) there cost = cost of i

        return dp[-1]
        
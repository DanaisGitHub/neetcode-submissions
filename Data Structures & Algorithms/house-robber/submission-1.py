class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if len(nums) == 1:
            return nums[-1]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        
        i = n-1
        dp[0]=nums[0]
        dp[1] = max(nums[0],nums[1])
        start = 1 if nums[0]>= nums[1] else 2
        for i in range(start,n):
            dp[i] =  max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
        
        
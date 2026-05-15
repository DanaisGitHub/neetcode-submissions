class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * n

        # if len(nums) == 1:
        #     return nums[-1]
        # if len(nums) == 2:
        #     return max(nums[0],nums[1])

        
        # i = n-1
        # dp[0]=nums[0]
        # dp[1] = max(nums[0],nums[1])
        # start = 1 if nums[0]>= nums[1] else 2
        # for i in range(start,n):
        #     dp[i] =  max(dp[i-1],dp[i-2]+nums[i])
        # return dp[-1]


        ## lets solve without mem


        # dp = either you can take curr,curr+2 or curr+1

        ## Not a clue how this works
        rob2,rob1 = 0,0
        for num in nums:
            temp = max(num + rob2,rob1)
            rob2 = rob1
            rob1 = temp
        return rob1

        # rob2 = i-2
        # rob1 = i-1

        # res = if curr + i-2 > i-1
        # i-2 = i-1
        # i-1 = res
        # rob1 = running total (aka 0..n)
        # rob2 = running total - 1 (0..n-1)
        # comparison = total with i-1 or total with i
        




        
        
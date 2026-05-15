class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        return max(self.algo(nums[1:]),self.algo(nums[:-1]))
    
    def algo(self,nums:List[int])->int:
        if len(nums) == 1:
            return nums[-1]
        rob2nd,rob1st = 0,0
        for num in nums:
            temp = max(rob1st,num+rob2nd)
            rob2nd = rob1st
            rob1st = temp
        return rob1st
        
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res:List[List[int]] = []
        subset:List[int] =[]
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            
            # skip any duplicates
        
            while i < len(nums)-1 and nums[i] == nums[i+1]: # if i is out of bounds 
                i+=1
            dfs(i+1)
            
        dfs(0)
        return res
        
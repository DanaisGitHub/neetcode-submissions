class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]: # what should you do with subsets that 
        # if it's unique add it in, if it already exists just different form then 
        # remeber the definition of a set (unique values)
        
        res:List[List[int]] = []
        nums.sort()
        
        def dfs(i:int,curArray:List[int]):
            # Base case
            if i >= len(nums):
                res.append(curArray.copy())
                return
            # may need another
            
            # should only create new braches for unique values
            # now great question are we to assume that all first values are unique,
            # I think no move i until i+1 != i
            # if I i =n the do 1
            
            
            
            curArray.append(nums[i])
            
            dfs(i+1,curArray)
            while i < len(nums)-1 and nums[i] == nums[i+1] : ## why did the pos matter?
                i += 1
            curArray.pop()
            dfs(i+1,curArray)
            
        dfs(0,[])     
        return res
            
            
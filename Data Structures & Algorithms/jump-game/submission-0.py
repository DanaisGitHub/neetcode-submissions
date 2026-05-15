class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i:int)->bool:
            if i >= len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            
            end = min(len(nums)-1,i+nums[i])+1

            for j in range (i+1,end): # i = current to what were on now
                if dfs(j):
                    return True
            return False
            
        return dfs(0)
            


        



            
            



        
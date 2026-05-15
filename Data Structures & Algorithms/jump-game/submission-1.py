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
            
        # greedy solution
        currGoal = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i+nums[i] >= currGoal: # currPos + maxJump >= goal
                currGoal = i #derement goal by i (could be more that 1)
            
        return True if currGoal == 0 else False
                
                


        #### 

            


        



            
            



        
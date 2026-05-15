class Solution:
    def jump(self, nums: List[int]) -> int:
        # recursion
        # brute force AF
        # for each possilbe jump take,then return the min
        #jumps = 0
        #i = 0
        #while i < len(nums)-1:
        #    endJump = min(len(nums)-1, i+nums[i])
        #    maxJumpI = (-1,-1)  # index, jump
        #    for j in range(i+1, endJump+1):
        #        if j == len(nums)-1:
        #            return jumps+1
        #        tempMaxJumpI = (j,nums[j]) # index + jump
        #        maxJumpI = maxJumpI if (maxJumpI[0]+maxJumpI[1])>=(tempMaxJumpI[0]+tempMaxJumpI[1]) else (tempMaxJumpI[0],tempMaxJumpI[1])
        #    i = maxJumpI[0]
        #    jumps+=1
#
#
        #return jumps



        def dfs (i:int,jumps:int)->int:
            if i == len(nums)-1:
                return jumps
            if nums[i] == 0:
                return float('inf')
            end = min(len(nums)-1,nums[i]+i)
            minJumps = float('inf')
            for j in range (i+1,end+1):
                minJumps = min(minJumps, dfs(j, jumps + 1)) #Find min jump for this round of jumps
            
            return minJumps
        return dfs(0,0)

      

        
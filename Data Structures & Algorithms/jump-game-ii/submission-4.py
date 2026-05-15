class Solution:
    def jump(self, nums: List[int]) -> int:
        # recursion
        # brute force AF
        # for each possilbe jump take,then return the min
        jumps = 0
        i = 0
        while i < len(nums)-1:
            endJump = min(len(nums)-1, i+nums[i])
            maxJumpI = (-1,-1)  # index, jump
            for j in range(i+1, endJump+1):
                if j == len(nums)-1:
                    return jumps+1
                tempMaxJumpI = (j,nums[j]) # index + jump
                maxJumpI = maxJumpI if (maxJumpI[0]+maxJumpI[1])>=(tempMaxJumpI[0]+tempMaxJumpI[1]) else (tempMaxJumpI[0],tempMaxJumpI[1])
            i = maxJumpI[0]
            jumps+=1


        return jumps


        return jumps

      

        
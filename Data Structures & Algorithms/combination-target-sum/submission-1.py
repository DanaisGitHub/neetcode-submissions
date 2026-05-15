class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
# plan of attack go through all combinations with duplicates
        # when the sum is above target base case
            # 
        # if sum == value base case
        
        res:List[List[int]] = []
        
        def myRec(i:int,currComb:List[int], total:int):
    
            if i>=len(nums) or total > target:
                return
            if total == target:
                res.append(currComb.copy())
                return
                
            currComb.append(nums[i])
            myRec(i,currComb, total + nums[i])
            
            currComb.pop()
            myRec(i+1,currComb,total)
            
        myRec(0,[],0)
        
        return res
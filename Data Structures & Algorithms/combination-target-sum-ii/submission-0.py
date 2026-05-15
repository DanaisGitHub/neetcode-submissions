class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ## same questtion but duplicates are in the sum 
        res:List[List[int]] = []
        candidates.sort()
        
        def dfs (i:int,curComb:List[int], total:int) ->None:
            if target == total:
                res.append(curComb.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            curComb.append(candidates[i])
            dfs(i+1,curComb,total + candidates[i])
            
            curComb.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,curComb, total)
            
        dfs(0,[],0)
        return res  
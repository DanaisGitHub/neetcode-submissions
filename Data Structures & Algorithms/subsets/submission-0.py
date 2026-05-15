class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # basic backtracking problem
        # so this problem is dfs search in a binary tree, but instead of looking for a node, 
        # you get each of the children

        # for back track you say either add this value or don't 2^n
        res =[] # return array
        subset = [] # each subset
        

        def dfs (i:int): # by using i, we back track i
            if i >= len(nums): # if there's nothing left to add
                res.append(subset.copy())
                return # I want to start forward to pop
            subset.append(nums[i])
            # apend
            dfs(i+1)
            subset.pop() # begins a branch where poped value doesn't exsit
            dfs(i+1)
        
        dfs(0)
        return res




        
        
        
        
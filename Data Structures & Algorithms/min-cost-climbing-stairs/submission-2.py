class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
         # recursion
        def recurion(i: int):
            if i>= len(cost):
                return 0
            return cost[i] + min(recurion(i+1), recurion(i+2))
        return min(recurion(0), recurion(1))

        # mem
        def rec(i: int, mem:dict[int,int]):
            if i>= len(cost):
                return 0
            if i in mem:
                return mem[i]
            
            mem[i] = cost[i] + min(rec(i+1), rec(i+2))
            
            return mem[i] 
        return min(rec(0,{1:1,2:2}), rec(1,{1:1,2:2}))

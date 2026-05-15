class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Lets bash our heads again :)

        def dfs(i: int):
            # 1 break down list to build back up
            if i >= len(nums):
                return [[]]

            res = []  # A global res will store [3] .... so wiping res after each back track is important
            perms = dfs(i+1)

            # well use i

            for p in perms:
                for j in range(len(p)+1):
                    pCopy: List[int] = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res  # eg returns [3] then [2,3],[3,2]

        return dfs(0)
        
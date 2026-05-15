class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # I sort of remember this question
        # something to do with sets and backing up

        numSet = set(nums)
        maxCount = 1
        if not nums:
            return 0

        for num in nums:
            counter = 1
            val = num
            while val - 1 in numSet: ## go to start of sequence
                val -=1
            
            while val+1 in numSet: ## cycle to end
                counter += 1
                val+=1
                maxCount = max(maxCount,counter)

        return maxCount


        
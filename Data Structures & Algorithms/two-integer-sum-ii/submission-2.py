class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r,l = 0, len(numbers) -1
        while r < l:
            res = numbers[l] + numbers[r] 
            if res > target:
                l -= 1
            elif res < target:
                r += 1
            else:
                return [r+1,l+1]
        
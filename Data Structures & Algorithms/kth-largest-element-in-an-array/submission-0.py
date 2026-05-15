class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap till I get a length of k, return first element
        # by th thoery this shouldn't work becuase children are not ordered 
        return heapq.nlargest(k,nums)[k-1]
        
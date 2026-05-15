from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # only keep k elements in the heap
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
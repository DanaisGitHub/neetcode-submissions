
class Solution:
    # Cannot do max heaps,min heaps with negated values
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: x*-1, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            heapq.heappush(stones, -1*abs(x-y))
            print(x,y,abs(x-y),stones)
        return stones[0] *-1



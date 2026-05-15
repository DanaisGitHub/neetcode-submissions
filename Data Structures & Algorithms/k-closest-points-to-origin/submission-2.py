class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        def eculidDistance(x1, y1, x2, y2): return (
            math.sqrt(abs(x1-x2) ** 2 + (abs(y1-y2)) ** 2))

        for point in points:
            point.insert(0, -1*eculidDistance(0, 0, point[0], point[1]))

        heapq.heapify(points)
        print(points)

        while len(points) > k:
            heapq.heappop(points)

        for p in points:
            res.append([p[1], p[2]])

        return res
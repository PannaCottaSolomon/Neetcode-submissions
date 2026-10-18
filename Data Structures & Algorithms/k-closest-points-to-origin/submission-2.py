import heapq
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        pointsMap = defaultdict(list)
        heap = []

        for point in points:
            x, y = point
            dist = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
            pointsMap[dist].append(point)
            heap.append(dist)

        heap = heapq.nsmallest(k, heap)
        # print(pointsMap.items())
        # print(heap)

        i = 0
        visited = set()
        while len(ans) < k:
            dist = heap[i]
            if dist not in visited:
                ans += pointsMap[dist]
                visited.add(dist)
            i += 1
        
        # print(ans)
        return ans
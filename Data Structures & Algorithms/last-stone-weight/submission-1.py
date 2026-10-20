import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) >= 2:
            w1 = heapq.heappop(maxHeap) * -1
            w2 = heapq.heappop(maxHeap) * -1
            heavier = max(w1, w2)
            lighter = min(w1, w2)
            if heavier > lighter:
                heapq.heappush(maxHeap, -(heavier - lighter))
            
        if len(maxHeap) == 0:
            return 0

        return -maxHeap[0]
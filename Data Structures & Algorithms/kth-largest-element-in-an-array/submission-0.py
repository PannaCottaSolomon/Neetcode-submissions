import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for val in nums:
            heapq.heappush(heap, val) 
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums[-k:]
        if len(self.heap) < k:
            self.heap = [-1001] * (k - len(self.heap)) + self.heap
        print(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) > 0:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        
        smallest = self.heap[0]
        print(self.heap)
        return smallest

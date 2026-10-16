import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums[-k:]
        # print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappushpop(self.heap, val)
        # print(self.heap)
        smallest = self.heap[0]
        return smallest

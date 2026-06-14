from heapq import heappop, heappush, heapify

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.size = nums, k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap)>self.size:
            heappop(self.heap)
        return self.heap[0]


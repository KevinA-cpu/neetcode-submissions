from heapq import heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.size=k
        for i in nums:
            heappush(self.heap, i)
        
        length = len(self.heap)
        for i in range(length-k):
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap)>self.size:
            heappop(self.heap)
        return self.heap[0]


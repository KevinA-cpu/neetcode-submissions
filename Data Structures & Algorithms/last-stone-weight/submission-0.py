from heapq import heappop, heappush




class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for weight in stones:
            heappush(heap, -weight)
        
        print(heap)
        while(heap):
            x, y = heappop(heap), None
            print(x)
            if heap:
                y = heappop(heap)
            elif y is None:
                return abs(x)
            

            if x == y:
                continue
            else:
                heappush(heap, x-y)
        
        return 0

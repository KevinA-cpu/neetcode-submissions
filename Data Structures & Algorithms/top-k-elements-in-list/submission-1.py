from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = {}
        for i in nums:
            if i not in answer:
                answer[i]=1
            else:
                answer[i]+=1
        
        # can be a bit more optimized
        heap=[]
        for i in answer:
            heappush(heap, (-answer[i],i))
        
        answer = []
        for i in range(k):
            answer.append(heappop(heap)[1])
        
        return answer
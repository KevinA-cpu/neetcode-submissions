from heapq import heappush, heappop


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in times:
            start = i[0]
            end=i[1]
            time=i[2]
            if start not in graph:
                graph[start] = [(end, time)]
            else:
                graph[start].append((end, time))

        visited=set()
        heap = []
        heappush(heap, (0,k))
        total=0
        while(heap):
            current = heappop(heap)
            if current[1] in visited:
                continue
            total = current[0]
            visited.add(current[1])
            if current[1] not in graph:
                continue

            for adjacent in graph[current[1]]:
                end=adjacent[0]
                time=adjacent[1]
                newTime=time + current[0]
                if end not in visited:
                    heappush(heap, (newTime, end))
                    print(heap)
                
        
        if len(visited) != n:
            return -1
        
        return total
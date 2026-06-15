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

        visited={k:0}
        heap = []
        heappush(heap, (0,k))
        while(heap):
            current = heappop(heap)
            if current[1] not in graph:
                continue

            for adjacent in graph[current[1]]:
                end=adjacent[0]
                time=adjacent[1]
                newTime=time + visited[current[1]]
                if end not in visited:
                    visited[end]=newTime
                    heappush(heap, (newTime, end))
                else:
                    if visited[end] > newTime:
                       visited[end]=newTime
                       heappush(heap, (newTime, end))
                    elif visited[end] == newTime:
                        continue
                
        
        if len(visited) != n:
            return -1
        
        total = 0
        print(visited)
        for i in visited:
            if total < visited[i]:
                total = visited[i]
        return total
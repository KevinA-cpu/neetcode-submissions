class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals always have ascending start_i
        # Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and 
        # also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.
        # newEnd < currentStart or newStart > currentEnd => no overlaps
        # newEnd >= currentStart and newStart <= currentEnd => overlaps
        if len(intervals)==0:
            intervals.append(newInterval)
            return intervals

        # O(m + m)
        result=[]
        newStart, newEnd = newInterval

        #
        insert = True
        for i, (start, end) in enumerate(intervals):
            if newEnd < start:
                result.append([newStart, newEnd])
                for j in range(i, len(intervals)):
                    result.append(intervals[j])
                insert=False
                break
            elif newStart > end:
                result.append([start,end])
            else:
                newStart = min(start,newStart)
                newEnd = max(end, newEnd)
        
        if insert:
            result.append([newStart, newEnd])
        
        return result

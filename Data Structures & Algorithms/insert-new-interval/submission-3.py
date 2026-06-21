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

        newStart, newEnd = newInterval
        notInserted=True
        for i in range(len(intervals)-1,-1,-1):
            start, end = intervals[i]
            if newStart >= start:
                #no overlap:
                if newEnd < start or newStart > end:
                    intervals.insert(i+1, [newStart, newEnd])
                else:
                    intervals[i][1] = max(end, newEnd)
                notInserted=False
                break
        
        if notInserted:
            intervals.insert(0, [newStart, newEnd])
        
        
        newInterval = []
        i = 0
        while(i<len(intervals)-1):
            curStart, curEnd = intervals[i]
            nextStart, nextEnd = intervals[i+1]
            if nextEnd >= curStart and nextStart <= curEnd:
                intervals[i][1] = max(curEnd, nextEnd)
                intervals.pop(i+1)
            else:
                i+=1


        
        return intervals

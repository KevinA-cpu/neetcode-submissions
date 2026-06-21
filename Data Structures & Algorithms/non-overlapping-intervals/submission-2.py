class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # nextStart >= curEnd or nextEnd <= curStart
        # nextStart < curEnd and nextEnd > curStart
        # [[-73, -26], [-65, -11], [-63, 2], [-62, -49], [-52, 31], [-40, -26], [-31, 49], [30, 47], [58, 95], [66, 98], [82, 97], [95, 99]]
        # [-73, -26] [30, 47] [58, 95] [95, 99]
        # [-62, -49] [-31, 49] [30, 47], [58, 95] [95, 99]
        # O(nlogn)
        intervals.sort()
        count=0
        length = len(intervals)
        memo={}
        curStart, curEnd = intervals[0]
        for i in range(1, length):
            nextStart, nextEnd = intervals[i]
            if nextStart < curEnd:
                curEnd=min(curEnd, nextEnd)
                count+=1
            else:
                curEnd=nextEnd

        return count

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # nextStart >= curEnd or nextEnd <= curStart
        # nextStart < curEnd and nextEnd > curStart
        # [[-73, -26], [-65, -11], [-63, 2], [-62, -49], [-52, 31], [-40, -26], [-31, 49], [30, 47], [58, 95], [66, 98], [82, 97], [95, 99]]
        # [-73, -26] [30, 47] [58, 95] [95, 99]
        # [-62, -49] [-31, 49] [30, 47], [58, 95] [95, 99]

        intervals.sort()
        count=0
        length = len(intervals)
        memo={}
        for i in range(length):
            if i in memo:
                continue
            curStart, curEnd = intervals[i]

            for j in range(i+1, length):
                if j in memo:
                    continue
                nextStart, nextEnd = intervals[j]

                if nextStart < curEnd and nextEnd > curStart:
                   curEnd=min(curEnd, nextEnd)
                   count+=1
                   memo[j]=True


        return count

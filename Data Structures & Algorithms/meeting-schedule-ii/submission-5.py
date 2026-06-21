"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # nextStart >= curEnd or nextEnd <= curStart
        # nextStart < curEnd and nextEnd > curStart
        if len(intervals) == 0:
            return 0
        #       1    2     3    4       5      6       5      6        5      6
        # [(0,10),(1,3),(2,6),(5,8),(7,12),(11,15),(13,18),(16,20),(19,25),(24,30)]
        # [(0,10),(1,3), (2,6)]
        intervals.sort(key=lambda d: d.start)
        rooms=[]
        heappush(rooms, (intervals[0].end, intervals[0].start))
    
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            earliestEndingRoom = rooms[0]
            if earliestEndingRoom[0] <= start:
                heappop(rooms)
                heappush(rooms, (end, start))
            else:
                heappush(rooms, (end, start))
          
        return len(rooms)


        
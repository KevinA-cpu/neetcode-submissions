"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # nextStart >= curEnd or nextEnd <= curStart
        # nextStart < curEnd and nextEnd > curStart
        if len(intervals) == 0:
            return 0
        #       1    2     3    4       5      6       5      6        5      6
        # [(0,10),(1,3),(2,6),(5,8),(7,12),(11,15),(13,18),(16,20),(19,25),(24,30)]
        # [(0,10),(5,8), (2,6)]
        intervals.sort(key=lambda d: d.start)
        rooms=[Interval(intervals[0].start, intervals[0].end)]
    
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            shouldCreateRoom = True

            for j in range(len(rooms)):
                if rooms[j].end <= start:
                    rooms[j].end=end
                    rooms[j].start
                    shouldCreateRoom=False
                    break

            if shouldCreateRoom:
                rooms.append(Interval(start, end))
          
        return len(rooms)


        
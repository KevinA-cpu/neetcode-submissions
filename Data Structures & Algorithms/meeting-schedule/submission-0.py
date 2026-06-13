"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# new.start < new.end
# old.start < old.end
# new.start >= old.end or new.end<=old.start
# reverse: new.start < old.end and new.end>old.start

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        calendar = []
        for i in intervals:
            for j in calendar:
                if j.start < i.end and j.end > i.start:
                    return False
            
            calendar.append(i)
        
        return True
            

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # nextEnd < curStart or nextStart > curEnd
        # nextEnd >= curStart and nextStart <= curEnd
        result = []
        length=len(intervals)
        memo={}
        for i in range(length):
            curStart, curEnd = intervals[i]
            if i in memo:
                continue

            for j in range(i+1, length):
                if j in memo:
                    continue
                nextStart, nextEnd = intervals[j]

                if nextEnd >= curStart and nextStart <= curEnd:
                    curStart = min(curStart, nextStart)
                    curEnd=max(curEnd, nextEnd)
                    memo[j]=True

            result.append([curStart, curEnd])
            memo[i] = True
        
        newMemo={}
        newResult = []
        newLength = len(result)
        for i in range(newLength):
            curStart, curEnd = result[i]

            if i in newMemo:
                continue

            for j in range(i+1, newLength):
                if j in newMemo:
                    continue
                nextStart, nextEnd = result[j]

                if nextEnd >= curStart and nextStart <= curEnd:
                    curStart = min(curStart, nextStart)
                    curEnd=max(curEnd, nextEnd)
                    newMemo[j]=True

            newResult.append([curStart, curEnd])
            newMemo[i] = True
        return newResult


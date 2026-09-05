from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        elif t == "":
            return ""
    
        minimumLength = len(t)
        length = len(s)
        if minimumLength > length:
            return ""

        tCounter = Counter(t)
        sCounter = Counter()
        l,r=0,0
        answer = None
        formed = -1
        seen = {}
        while(l<=r):
            while(r<length):
                if s[r] in tCounter:
                    sCounter.update(s[r])
                    formed = r
                    if sCounter[s[r]] >= tCounter[s[r]]:
                        seen[s[r]] = True
                    # Stop when seen compasses tCounter
                    if len(seen) == len(tCounter):
                        break
                r+=1
            
            while(l<length):
                if s[l] in sCounter:
                    sCounter[s[l]]-=1
                    # Stop shrink when sCounter can no longer
                    # encompass tCounter
                    if sCounter[s[l]] < tCounter[s[l]]:
                        sCounter.update(s[l])
                        break
                l+=1
            
            if answer == None and len(seen) == len(tCounter):
                answer = (l,formed+1)
            elif answer is not None and (answer[1] - answer[0]) > (formed+1 - l):
                answer= (l,formed+1)
            
            if r == length:
                break

            del seen[s[r]]
            r+=1

        return "" if answer is None else s[answer[0]:answer[1]]

            

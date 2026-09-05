from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
    
        minimumLength = len(t)
        length = len(s)
        if minimumLength > length:
            return ""

        tCounter = Counter(t)
        sCounter = Counter()
        l,r=0,0
        answer = ""
        formed = -1
        seen = {}
        while(l<=r):
            while(r<length):
                if s[r] in tCounter:
                    sCounter.update(s[r])
                    formed = r
                    if sCounter[s[r]] >= tCounter[s[r]]:
                        seen[s[r]] = True
                    if len(seen) == len(tCounter):
                        break
                r+=1
            
            while(l<length):
                if s[l] in sCounter:
                    sCounter[s[l]]-=1
                    if sCounter[s[l]] < tCounter[s[l]]:
                        sCounter.update(s[l])
                        break
                l+=1
            
            tempStr = s[l:formed+1]
            if answer == "" and len(seen) == len(tCounter):
                answer = tempStr
            elif len(answer) > len(tempStr):
                answer=tempStr
            
            if r == length:
                break

            del seen[s[r]]
            r+=1

        return answer

            

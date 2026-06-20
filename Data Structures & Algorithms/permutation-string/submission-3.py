


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        lens1=len(s1)
        lens2=len(s2)

        for i in range(lens1-1,lens2):
            count=0
            freq={}
            for j in range(l, i+1):
                if s2[j] not in freq:
                    freq[s2[j]] = 1
                else:
                    freq[s2[j]] +=1
            
            for j in s1:
                if j not in freq:
                    break
                else:
                    freq[j]-=1

            answer=True
            for j in freq:
                if freq[j] != 0:
                    answer=False
                    break
            
            if answer:
                return True

            l+=1
        return False
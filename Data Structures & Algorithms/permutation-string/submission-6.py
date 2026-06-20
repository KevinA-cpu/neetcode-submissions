


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        lens1=len(s1)
        lens2=len(s2)
        freqS1={}
        for i in s1:
            if i not in freqS1:
                freqS1[i]=1
            else:
                freqS1[i]+=1

        freqS2=None
        for i in range(lens1-1,lens2):
            count=0
            if freqS2 is None:
                freqS2={}
                for j in range(l, i+1):
                    if s2[j] not in freqS2:
                        freqS2[s2[j]] = 1
                    else:
                        freqS2[s2[j]] +=1
            else:
                freqS2[s2[l-1]]-=1
                if freqS2[s2[l-1]] == 0:
                    del freqS2[s2[l-1]]

                if s2[i] not in freqS2:
                    freqS2[s2[i]] = 1
                else:
                    freqS2[s2[i]] +=1

            
            if freqS2==freqS1:
                return True

            l+=1
        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstMap = {}
        for i in s:
            if i in firstMap:
                firstMap[i]+=1
            else:
                firstMap[i]=1

        secondMap = {}
        for i in t:
            if i in secondMap:
                secondMap[i]+=1
            else:
                secondMap[i]=1
        
        return firstMap == secondMap
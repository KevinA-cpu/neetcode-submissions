class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        if length == 0:
            return 0

        l, r= 0,1
        longest=1
        counter=1
        for i in range(1, length):
            shouldExpand=True
            for j in range(l, r):
                if s[j] == s[i]:
                    if (r-l)>longest:
                        longest=(r-l)
                    l=j+1
                    r+=1
                    print(l, r)
                    shouldExpand=False
                    break
            
            if shouldExpand:
                r+=1
                print(l, r)
                if (r-l)>longest:
                    longest=(r-l)
        print(l, r)
        if (r-l)>longest:
            longest=(r-l)
        return longest

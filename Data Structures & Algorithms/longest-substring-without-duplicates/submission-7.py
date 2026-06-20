class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        if length == 0:
            return 0

        hashMap = set()
        l=0
        longest=1

        for r in range(len(s)):
            while s[r] in hashMap:
                hashMap.remove(s[l])
                l+=1
            hashMap.add(s[r])
            longest = max(longest,r-l+1 )

        return longest

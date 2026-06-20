class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        longest=0
        freq = {}

        curFreq = 0
        curChar=""

        l=0
        freq[s[0]] = 1
        for i in range(1,length):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] +=1
            
            if freq[s[i]] > curFreq:
                curChar=s[i]
                curFreq=freq[s[i]]
            
            remainder = ((i - l) + 1) - curFreq
            while(remainder > k):
                freq[s[l]]-=1
                remainder-=1
                l+=1
            
            if remainder + curFreq > longest:
                longest = remainder + curFreq

        return longest
        
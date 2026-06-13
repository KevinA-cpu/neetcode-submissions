class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            elif i in hashMap:
                hashMap[i]+=1
        
        for i in hashMap:
            if hashMap[i] == 1:
                return i
        
        return -1
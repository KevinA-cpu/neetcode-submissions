class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                 hashMap[i]+=1
        
        for i in hashMap:
            if hashMap[i] >=2:
                return True
        return False
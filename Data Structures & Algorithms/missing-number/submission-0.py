class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        for i in range(len(nums)+1):
            start = start ^ i
        
        for i in nums:
            start = start ^ i
        
        return start
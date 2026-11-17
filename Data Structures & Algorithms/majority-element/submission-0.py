class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        majority = length // 2
        counter = Counter(nums)
        for i in counter:
            if counter[i] > majority:
                return i
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length=len(nums)
        tab = [1] * length
        longest=1
        for i in range(length):
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    tab[i] = max(tab[j]+1, tab[i])
                    if tab[i] > longest:
                        longest=tab[i]
        return longest
            
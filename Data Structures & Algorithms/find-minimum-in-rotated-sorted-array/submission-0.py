class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minimum = 1001
        while(l<=r):
            mid = l + (r-l)//2
            print(mid, l, r)
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] <= nums[r]:
                r = mid - 1

            if minimum == 1001 or minimum > nums[mid]:
                minimum = nums[mid]
        return minimum

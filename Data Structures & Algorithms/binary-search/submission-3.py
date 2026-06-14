class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l, r = 0, length-1
        half = (r+l) // 2
        # 6, r = 0, l = 5, half=2                                              
        if l == r and nums[r] == target:
            return l
        while(l <= r):
            # current = 6
            current = nums[half]

            if target > current:
                l = half+1
                # l = 3
                # half = 4
                half = (l+r)//2
            elif target < current:
                r = half-1
                # r=3, l=3
                # half = 
                half = (l+r)//2
            else:
                return half
    
        return -1
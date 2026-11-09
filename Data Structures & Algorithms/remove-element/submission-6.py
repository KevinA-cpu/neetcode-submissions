class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r = 0, len(nums)-1
        if l == r and nums[l] != val:
            return 1

        k = 0
        length = len(nums)
        while(l < r):

            while(r >=0 and nums[r] == val):
                r-=1
            
            while(l < length and nums[l] != val):
                k+=1
                l+=1
            
            if l >= r:
                break
 
            nums[l] = nums[r]
            nums[r] = val
            r-=1

            if l >= r:
                k+=1
        
        return k

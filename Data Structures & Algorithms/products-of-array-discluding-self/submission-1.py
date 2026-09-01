class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        length = len(nums)

        lookupPrefix = {}
        for i in range(0, length):
            product = product * nums[i]
            lookupPrefix[i] = product
        
        
        lookupSuffix = {}
        product = 1
        for i in range(length-1, -1, -1):
            product = product * nums[i]
            lookupSuffix[i] = product

        for i in range(0, length):
            temp = 1
            if i - 1 in lookupPrefix:
                temp *= lookupPrefix[i-1]
            
            if i+1 in lookupSuffix:
                temp *= lookupSuffix[i+1]

            ans.append(temp)
            

        return ans

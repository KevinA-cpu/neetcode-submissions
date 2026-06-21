class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k

        answer=[]
        while(l<r and r<=len(nums)):
            maximum=float('-Inf')
            for i in range(l, r):
                if nums[i]>maximum:
                    maximum=nums[i]
            answer.append(maximum)
            l+=1
            r+=1

        return answer
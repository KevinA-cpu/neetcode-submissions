class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find the maximum distance * min(heights[l], heights[r])
        length = len(heights)
        answer=0
        l, r = 0, length-1
        while(l < r):
            volume = min(heights[l], heights[r]) * (r-l)
            if volume>answer:
                answer=volume

            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        return answer
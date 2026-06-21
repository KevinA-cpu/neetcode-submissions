class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        queue = deque()  # index
        l, r = 0, k

        for i in range(l, r):
            if queue:
                while(queue and nums[queue[-1]] < nums[i]):
                    queue.pop()
                queue.append(i)
            else:
                queue.append(i)

        output.append(nums[queue[0]])

        while r < len(nums):
          l+=1
          if l > queue[0]:
            queue.popleft()

          r+=1
          while(queue and nums[queue[-1]] < nums[r-1]):
                queue.pop()
          queue.append(r-1)
          output.append(nums[queue[0]])

        return output
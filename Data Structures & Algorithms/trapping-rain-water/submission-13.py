class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        length = len(height)
        # i = 0
        # while(i<length and height[i] == 0):
        #     i+=1

        # j = i + 1
        # while(i < length):
        #     firstBar = height[i]
        #     barInBetweens = 0
        #     try:
        #         # find a bar higher than height[i]
        #         while(j < length and height[j] < firstBar):
        #             if height[j] != 0:
        #                 barInBetweens += height[j]
        #             j+=1

        #         if j != length:
        #             raise ValueError("BarFound") 

        #         # find a height[j] that is bigger than the smallest
        #         # height between i and j
        #         j=i+1
        #         barInBetweens=0
        #         lowestBar = height[j]
        #         while(lowestBar >= height[j]):
        #             if height[j] < lowestBar:
        #                 lowestBar = height[j]
        #             j+=1
                
        #         if j != length:
        #             # check if there is a bigger bar behind or not:
        #             for k in range(j+1, length):
        #                 if height[k] > height[j]:
        #                     j = k
                
        #             for k in range(i+1, j):
        #                 if height[k] >= height[j]:
        #                     barInBetweens+= height[j]
        #                 else:
        #                     barInBetweens+= height[k]

        #     except IndexError:
        #         i += 1
        #         j = i + 1
        #         continue
        #     except ValueError:
        #         pass
            
        #     water+=(min(firstBar, height[j]) * (j-i-1)) - barInBetweens
        #     i = j
        #     j = i + 1
        # Optimal solution below:
        l, r = 0, length - 1
        leftMax, rightMax = height[l], height[r]
        while(l<r):
            if leftMax > rightMax:
                r -= 1
                if height[r] > rightMax:
                    rightMax = height[r]
                water+=(rightMax - height[r])
            else:
                l+=1
                if height[l] > leftMax:
                    leftMax = height[l]
                water+=(leftMax - height[l])


        return water
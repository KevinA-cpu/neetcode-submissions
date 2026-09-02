class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0

        nums.sort()
        highest = 1
        counter = 1
        print(nums)
        for i in range(1, length):
            if nums[i] - nums[i-1] > 1:
                counter = 1
                continue
            elif nums[i] == nums[i-1]:
                continue


            counter+=1
            if counter > highest:
                highest = counter 
        
        return highest




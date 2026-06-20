class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1 brute force
        # 2 sort 
        #  [-4,-1,-1,0,1,2]
        length = len(nums)
        nums.sort()
        answer =[]
        l, r = 0, length-1
        memo={}
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r=length-1
            currentTarget = nums[i]

            while(l<r):
                if -currentTarget == (nums[l]+nums[r]):
                    answer.append([nums[l], nums[i], nums[r]])
                    l+=1
                    while(l+1 < length and nums[l-1] == nums[l]):
                        l+=1
                else:
                    if -currentTarget > nums[l]+nums[r]:
                        l+=1
                    else:
                        r-=1

        return answer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        l, r=0,length-1
        while((numbers[l] + numbers[r]) != target):
           if numbers[l] + numbers[r] > target:
             r-=1
           else:
             l+=1


        return [l+1, r+1]
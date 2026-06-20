class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r=0,1
        length = len(numbers)
        while((numbers[l] + numbers[r]) != target):
            r+=1
            if r == length:
               l+=1
               r=l+1


        return [l+1, r+1]
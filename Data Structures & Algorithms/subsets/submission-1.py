class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        subset = []
        length = len(nums)
        def dfs(i):
            if i == length:
                newCopy = [x for x in subset]
                answer.append(newCopy)
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return answer
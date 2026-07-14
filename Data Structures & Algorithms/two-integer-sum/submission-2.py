class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for index, value in enumerate(nums):
            if target-value not in mapper:
                mapper[target-value] = index
            else:
                return [mapper[target-value], index]

            if value in mapper and mapper[value] != index:
                return [mapper[value], index]

        return []
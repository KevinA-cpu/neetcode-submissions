class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while(l<=r):
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif r == l:
                break
            # assume that left half is sorted
            elif nums[mid] > nums[r]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    if target < nums[r]:
                        l = mid + 1
                    elif target == nums[r]:
                        return r
                    else:
                        r = mid - 1
            # assume that right half is sorted
            elif nums[mid] < nums[r]:
                if target > nums[mid]:
                    if target < nums[r]:
                        l = mid + 1
                    elif target == nums[r]:
                        return r
                    else:
                        r = mid - 1
                elif target < nums[mid]:
                    r = mid - 1
        
        return -1
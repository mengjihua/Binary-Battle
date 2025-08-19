from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(i: int) -> bool:
            x = nums[i]
            if x > nums[r]:
                return target > nums[r] and x >= target
            return target > nums[r] or x >= target
        
        l, r = 0, len(nums) - 2
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[r]:
                r -= 1
            elif check(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return nums[r] == target
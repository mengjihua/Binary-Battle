from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        
        pre_sum = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                pre_sum += nums[i]
            else:
                break
        
        nums = set(nums)
        for i in range(pre_sum, sum(nums) + 1):
            if i not in nums:
                return i
        return sum(nums) + 1
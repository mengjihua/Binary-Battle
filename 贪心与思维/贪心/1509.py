from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()
        ans = float('inf')

        for i in range(4):
            ans = min(ans, abs(nums[n + i - 4] - nums[i]))
        return ans
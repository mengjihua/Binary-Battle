from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n, min_num, ans = len(nums), nums[0], -1
        for i in range(1, n):
            ans = max(ans, nums[i] - min_num)
            min_num = min(min_num, nums[i])
        return ans if ans != 0 else -1
from typing import List
# https://leetcode.cn/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = 1
            for j in range(1, i):
                if nums[j - 1] < nums[i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
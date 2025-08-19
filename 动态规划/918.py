from typing import List
# https://leetcode.cn/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
        return max(dp[1:])

# 测试
if __name__ == "__main__":
    solution = Solution()
    nums = [1,-2,3,-2]
    print(Solution().maxSubarraySumCircular(nums)) # 输出: 3
    print(solution.maxSubarraySumCircular(nums=[5,-3,5])) # 输出: 10
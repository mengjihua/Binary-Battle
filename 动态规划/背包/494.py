from typing import List
from functools import cache
# https://leetcode.cn/problems/target-sum/

class Solution:
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        @cache
        def f(depth, n, num):
            if depth == n:
                return 1 if num == target else 0
        
            first = f(depth + 1, n, num + nums[depth])
            second = f(depth + 1, n, num - nums[depth])
            
            return first + second

        return f(0, len(nums), 0)

    # 使用动态规划
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0] * 2001 for _ in range(n + 1)]
        dp[0][1000] = 1

        for i in range(1, n + 1):
            for j in range(2001):
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
                if j + nums[i - 1] < 2001:
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]

        return dp[n][target + 1000]

# 测试
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(solution.findTargetSumWays(nums, target)) # 输出: 5
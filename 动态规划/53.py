from typing import List
# https://leetcode.cn/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = max(dp[i - 1] + nums[i - 1], nums[i - 1])
        #     print(dp[i], nums[i - 1], dp[i - 1])
        # print(dp)
        return max(dp[1:])

# 测试
if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(solution.maxSubArray(nums)) # 输出: 6
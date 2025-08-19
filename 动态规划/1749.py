from typing import List
# https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp1, dp2 = [0] * (n + 1), [0] * (n + 1)
        for i in range(1, n + 1):
            dp1[i] = max(dp1[i - 1] + nums[i - 1], nums[i - 1])
            dp2[i] = max(dp2[i - 1] - nums[i - 1], -nums[i - 1])
        # print(dp1, dp2)
        return max(max(dp1), max(dp2))

# 测试
if __name__ == "__main__":
    solution = Solution()
    nums = [2,-5,1,-4,3,-2]
    print(solution.maxAbsoluteSum(nums)) # 输出: 8
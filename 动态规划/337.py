from typing import List
from functools import cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # @cache
        # def f(num):
        #     if num == target:
        #         return 1
        #     elif num > target:
        #         return 0
        #     res = 0
        #     for i in range(len(nums)):
        #         res += f(num + nums[i])
        #     return res
        
        # return f(0)

        # @cache
        # def f(num):
        #     if num == 0:
        #         return 1
        #     elif num < 0:
        #         return 0
        #     res = 0
        #     for i in range(len(nums)):
        #         res += f(num - nums[i])
        #     return res
        # return f(target)

        nums.sort()
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(n):
                if i < nums[j]:
                    break
                dp[i] += dp[i - nums[j]]
        return dp[target]
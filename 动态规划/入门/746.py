from typing import List
from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # @cache
        # def f(i):
        #     if i <= 1:
        #         return 0
            
        #     return min(f(i - 1) + cost[i - 1], f(i - 2) + cost[i - 2])
            
        # return f(len(cost))
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
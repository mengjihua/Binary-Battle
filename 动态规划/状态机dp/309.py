from typing import List
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
            dp[i][2] = dp[i - 1][1] + prices[i]
        # print(dp)
        return 0 if max(dp[n - 1]) <= 0 else max(dp[n - 1])
from typing import List
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[float('-inf'), float('-inf')] for _ in range(k + 1)] for _ in range(n)]

        for i in range(k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        for i in range(1, n):
            dp[i][0][0] = 0 
        
        ans = 0
        for i in range(1, n):
            for j in range(1, min(k, i + 1) + 1):
                dp[i][j][0] = max(dp[i - 1][j][1] + prices[i], dp[i - 1][j][0])
                dp[i][j][1] = max(dp[i - 1][j - 1][0] - prices[i], dp[i - 1][j][1])
                ans = max(dp[i][j][0], dp[i][j][1], ans)

        # print(dp[n - 1])
        return ans
    
# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit(2, [3,2,6,5,0,3]))
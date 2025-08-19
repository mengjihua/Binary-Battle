from typing import List
from functools import cache
# from functools import lru_cache
# import sys
# sys.setrecursionlimit(10 ** 6)
# https://leetcode.cn/problems/coin-change/

class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     @lru_cache(None)
    #     def f(depth, n, num):
    #         print(depth, num)
    #         if num == amount:
    #             return depth
    #         elif num > amount:
    #             return float('inf')
    #         else:
    #             res = float('inf')
    #             for i in range(n):
    #                 res = min(res, f(depth + 1, n, num + coins[i]))
    #         return res
        
    #     ans = f(0, len(coins), 0)
    #     return ans if ans != float('inf') else -1
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        # for i in range(n + 1):
        #     dp[i][0] = 0
        
        # for i in range(1, n + 1):
        #     for j in range(1, amount + 1):
        #         if j < coins[i - 1]:
        #             dp[i][j] = dp[i - 1][j]
        #         else:
        #             dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
        # return dp[n][amount] if dp[n][amount] != float('inf') else -1
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(coins[i - 1], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i - 1]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    
# 测试
if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    ans = Solution().coinChange(coins, amount)
    print(ans)  # 输出: 3
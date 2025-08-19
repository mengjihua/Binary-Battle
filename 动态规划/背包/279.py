import math

class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_num = int(math.sqrt(n))
        if pow(sqrt_num, 2) == n:
            return 1

        max_num = int(math.sqrt(n))

        dp = [[float('inf')] * (n + 1) for _ in range(max_num + 1)]
        for i in range(max_num + 1):
            dp[i][0] = 0
        
        for i in range(1, max_num + 1):
            for j in range(n + 1):
                if j < i ** 2:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - i ** 2] + 1)
        # print(dp)
        return dp[max_num][n]

    def numSquares2(self, n: int) -> int:
        sqrt_num = int(math.sqrt(n))
        if pow(sqrt_num, 2) == n:
            return 1

        max_num = int(math.sqrt(n))

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, max_num + 1):
            for j in range(i ** 2, n + 1):
                dp[j] = min(dp[j], dp[j - i ** 2] + 1)
        return dp[n]

# 测试
n = 11
print(Solution().numSquares(n))  # 输出: 3 (11 = 3^2 + 1^2 + 1^2)
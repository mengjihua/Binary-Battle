from functools import lru_cache
from typing import List
# https://leetcode.cn/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0
            if l == r:
                return 
            
            if s[l] == s[r]:
                return 2 + dfs(l + 1, r - 1)
            return max(dfs(l + 1, r), dfs(l, r - 1))
        return dfs(0, len(s) - 1)

    def longestPalindromeSubseq1(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # i > j 时，dp[i][j] = 0s
        # i == j 时，dp[i][j] = 1
        # dp[i][j] = dp[i + 1][j - 1] + 2 if s[i] == s[j] else max(dp[i + 1][j], dp[i][j - 1])
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 2)
        return dp[0][n - 1]

    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        reversed_s = s[::-1]
        if s == reversed_s:
            return n
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == reversed_s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n]

# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindromeSubseq1("abcdef"))  # 输出: 1
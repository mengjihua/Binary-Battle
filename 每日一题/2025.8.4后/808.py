from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
def input(): return stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4451:
            return 1

        @lru_cache(None)
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0

            return 0.25 * (
                dfs(a - 100, b) +
                dfs(a - 75, b - 25) +
                dfs(a - 50, b - 50) +
                dfs(a - 25, b - 75)
            )
        return dfs(n, n)

    # 期望dp
    def soupServings(self, n: int) -> float:
        if n >= 4451:
            return 1.0

        # 缩放到 25ml 为一个单位
        N = ceil(n / 25)

        dp = [[0.0] * (N + 1) for _ in range(N + 1)]
        dp[0][0] = 0.5
        for i in range(1, N + 1):
            dp[0][i] = 1.0

        for a in range(1, N + 1):
            for b in range(1, N + 1):
                dp[a][b] = 0.25 * (
                    dp[max(a - 4, 0)][b] +
                    dp[max(a - 3, 0)][max(b - 1, 0)] +
                    dp[max(a - 2, 0)][max(b - 2, 0)] +
                    dp[max(a - 1, 0)][max(b - 3, 0)]
                )

        return dp[N][N]


# 预处理最大范围
MAX_N = 180
# 创建 DP 表
dp = [[0.0] * (MAX_N + 1) for _ in range(MAX_N + 1)]

# 边界
dp[0][0] = 0.5
for b in range(1, MAX_N + 1):
    dp[0][b] = 1.0
for a in range(1, MAX_N + 1):
    dp[a][0] = 0.0

# 自底向上填表
for a in range(1, MAX_N + 1):
    for b in range(1, MAX_N + 1):
        dp[a][b] = 0.25 * (
            dp[max(a - 4, 0)][b] +
            dp[max(a - 3, 0)][max(b - 1, 0)] +
            dp[max(a - 2, 0)][max(b - 2, 0)] +
            dp[max(a - 1, 0)][max(b - 3, 0)])

    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        if m >= MAX_N:
            return 1.0
        return dp[m][m]

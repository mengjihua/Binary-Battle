from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    # 以下定义[i, j]: 表示沿边从顶点 i 顺时针到顶点 j, 再加上直接从 j 到 i 的边所围成的多边形
    # 记忆化搜索
    def minScoreTriangulation(self, values: List[int]) -> int:
        '''
            n == values.length
            3 <= n <= 50
            1 <= values[i] <= 100
        '''
        n = len(values)
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            if j - i + 1 < 3:
                return 0
            return min(dfs(i, k) + dfs(k, j) + values[i] * values[k] * values[j] for k in range(i + 1, j))
        return dfs(0, n - 1)
        
    # 动态规划
    def minScoreTriangulation2(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = inf
                for k in range(i + 1, j):
                    dp[i][j] = fmin(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])
        return dp[0][n - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.minScoreTriangulation(values = [1,2,3]))
    print(s.minScoreTriangulation(values = [3,7,4,5]))
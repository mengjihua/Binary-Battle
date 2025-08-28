from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        @lru_cache(maxsize=None)
        def dfs(i, j, dir_k, target, turn):
            i, j = i + directions[dir_k][0], j + directions[dir_k][1]
            if not (0 <= i < n and 0 <= j < m) or grid[i][j] != target:
                return 1
            res = 1 + dfs(i, j, dir_k, 2 - target, turn)
            if not turn:
                res = _max(res, 1 + dfs(i, j, (dir_k + 1) % 4, 2 - target, True))
            return res

        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for k in range(4):
                        ans = _max(ans, dfs(i, j, k, 2, False))

        return ans
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
    # 柱状图思想
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        # 计算每一列的高度
        col_height = [0] * n
        for i in range(m):
            for j in range(n):
                col_height[j] = col_height[j] + 1 if mat[i][j] == 1 else 0
                hi_limit = inf  # 以(i, j)为点的矩形的高度限制
                for k in range(j, -1, -1):
                    if col_height[k] == 0:
                        break
                    hi_limit = _min(hi_limit, col_height[k])
                    ans += hi_limit
        return ans

    # 单调栈
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        col_height = [0] * n
        for i in range(m):
            for j in range(n):
                col_height[j] = col_height[j] + 1 if mat[i][j] == 1 else 0
            stack = [(-1, 0, -1)]
            for r, h in enumerate(col_height):
                while stack and stack[-1][2] >= h:
                    stack.pop()
                l, prev, _ = stack[-1]
                cur = prev + (r - l) * h
                ans += cur
                stack.append((r, cur, h))
        return ans
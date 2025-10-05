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
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7


class PrefixSum:
    def __init__(self, nums: list, is2D: bool = False):
        if is2D:
            self.preSum = self.getPrefixSum2D(nums)
        else:
            self.preSum = self.getPrefixSum1D(nums)

    def getPrefixSum2D(self, nums: list) -> list:
        m, n = len(nums), len(nums[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + nums[i - 1][j - 1]
        return pre
    
    def getPrefixSum1D(self, nums: list) -> list:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        return pre

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pre = PrefixSum(grid, True).preSum
        
        ans = 0
        for x_length in range(1, m + 1):
            for y_length in range(1, n + 1):
                sm = pre[x_length][y_length]
                if sm <= k: ans += 1
                else: break
        return ans
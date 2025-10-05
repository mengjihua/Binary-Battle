from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right, insort
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
    # 暴力, TLE
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = PrefixSum(matrix, True).preSum
        
        ans = -inf
        for x1 in range(m):
            for y1 in range(n):
                for x2 in range(x1, m):
                    for y2 in range(y1, n):
                        sm = pre[x2 + 1][y2 + 1] - pre[x1][y2 + 1] - pre[x2 + 1][y1] + pre[x1][y1]
                        if sm <= k: ans = fmax(ans, sm)
        return ans
    
    # TODO: 二维前缀和(四循环, 维护两个点, 即x1, y1, x2, y1) -> 一维前缀和(三循环, 维护两列 + 行数) + 有序集合
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        
        ans = -inf
        for y1 in range(n):
            for y2 in range(y1, n):
                sms = SortedList([0])
                sm = 0
                for x in range(m):
                    sm += matrix[x][y2] - (0 if y1 == 0 else matrix[x][y1 - 1])
                    idx = sms.bisect_left(sm - k)
                    if idx != len(sms):
                        ans = fmax(ans, sm - sms[idx])
                    sms.add(sm)
        return ans
    
    # 维护有序列表 -> 二分查找 + 插入
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        
        ans = -inf
        for y1 in range(n):
            for y2 in range(y1, n):
                sms = [0]
                sm = 0
                for x in range(m):
                    sm += matrix[x][y2] - (0 if y1 == 0 else matrix[x][y1 - 1])
                    idx = bisect_left(sms, sm - k)
                    if idx < len(sms):
                        ans = fmax(ans, sm - sms[idx])
                    insort(sms, sm)
        return ans
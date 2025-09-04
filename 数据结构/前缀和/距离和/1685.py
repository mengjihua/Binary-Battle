from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
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
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre = list(accumulate(nums, initial=0))
        n = len(nums)
        res = []
        for i, num in enumerate(nums):
            l = num * i - pre[i]
            r = pre[-1] - pre[i + 1] - num * (n - i - 1)
            res.append((l + r))
        return res

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 记录 (值, 原始索引) ，并按值排序
        num_idx_map = [(nums[i], i) for i in range(n)]
        num_idx_map.sort()
        
        # 提取排序后的值，计算前缀和
        sorted_nums = [num for num, _ in num_idx_map]
        pre = list(accumulate(sorted_nums, initial=0))
        
        # 为排序后的每个位置计算 res
        res = [0] * n
        for i, (num, orig_idx) in enumerate(num_idx_map):
            l = i * num - pre[i]
            r = pre[n] - pre[i + 1] - num * (n - 1 - i)

            res[orig_idx] = l + r
        
        return res
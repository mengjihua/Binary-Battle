from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate, pairwise
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, comb, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

nums1 = [1, 2]
nums2 = [2, 3]

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        w = [[0] * n for _ in range(n)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                w[i][j] = x ^ y
        @lru_cache(None)
        def f(s):
            if s == 0:
                return 0
            i = n - s.bit_count()
            return min(f(s ^ (1 << j)) + w[i][j] for j in range(n) if s & (1 << j))
        return f((1 << n) - 1)
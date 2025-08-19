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
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        hi = [0] * m
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    hi[j] += 1
                else:
                    hi[j] = 0
            # nums = sorted(hi)
            # j = 0
            # while j < m:
            #     ans = max(ans, nums[j] * (m - j))
            #     j = bisect_right(nums, nums[j])    # TODO: 二分优化, 到下一个不同的元素
            for j, h in enumerate(sorted(hi)):
                ans = max(ans, h * (m - j))
        return ans
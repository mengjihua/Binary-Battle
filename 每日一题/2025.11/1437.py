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

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        last_idx = 0
        while last_idx < n and nums[last_idx] == 0:
            last_idx += 1
        for i in range(last_idx + 1, n):
            if nums[i] == 1:
                if i - last_idx - 1 < k:
                    return False
                last_idx = i
        return True
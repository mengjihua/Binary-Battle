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

def get(num):
    m = len(bin(num)) - 2
    res = sum(ceil(i / 2) << (i - 1) for i in range(1, m))
    return res + ceil(m / 2) * (num + 1 - (1 << (m - 1)))

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # def get(num):
        #     i = base = 1
        #     cnt = 0
        #     while base <= num:
        #         cnt += ((i + 1) // 2) * (_min(base * 2 - 1, num) - base + 1)
        #         i += 1
        #         base *= 2
        #     return cnt
        
        ans = 0
        for l, r in queries:
            ans += ceil((get(r) - get(l - 1)) / 2)
        return ans
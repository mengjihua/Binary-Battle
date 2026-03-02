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
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for l in range(n):
            c_cnt = [0] * 26
            mx = cnt = 0
            for r in range(l, n):
                c_ord = ord(s[r]) - ord('a')
                if c_cnt[c_ord] == 0: cnt += 1
                c_cnt[c_ord] += 1
                mx = fmax(mx, c_cnt[c_ord])
                if mx * cnt == r - l + 1: ans = fmax(ans, r - l + 1)
        return ans
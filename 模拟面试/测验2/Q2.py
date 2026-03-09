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
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        n = len(s)
        
        for c in 'QWER':
            cnt[c] = cnt[c] - n // 4
        if all(cnt[c] == 0 for c in 'QWER'):
            return 0
        
        w = defaultdict(int)
        res, l = inf, 0
        for r in range(n):
            w[s[r]] += 1
            while all(w[c] >= cnt[c] for c in 'QWER'):
                res = fmin(res, r - l + 1)
                w[s[l]] -= 1
                l += 1
        return res
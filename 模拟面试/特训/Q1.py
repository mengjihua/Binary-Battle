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
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if m < n:
            return []

        res = []
        p_cnt = Counter(p)
        cnt = defaultdict(int)
        for r in range(m):
            cnt[s[r]] += 1
            if r < n - 1:
                continue
            if cnt == p_cnt:
                res.append(r - n + 1)
            cnt[s[r - n + 1]] -= 1
            if cnt[s[r - n + 1]] == 0:
                del cnt[s[r - n + 1]]
        return res
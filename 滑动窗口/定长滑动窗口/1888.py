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
    def minFlips(self, s: str) -> int:
        ans = n = len(s)
        cnt = 0
        for r in range(n * 2 - 1):
            if int(s[r % n]) % 2 != r % 2:
                cnt += 1

            l = r - n + 1
            if l < 0: continue

            ans = min(ans, cnt, n - cnt)
            if ord(s[l]) % 2 != l % 2:
                cnt -= 1
        return ans
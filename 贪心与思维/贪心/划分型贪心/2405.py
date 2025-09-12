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

class Solution:
    def partitionString(self, s: str) -> int:
        cnt = defaultdict(int)
        ans, l = 1, 0
        for c in s:
            if cnt[c] == 1:
                ans += 1
                cnt.clear()
                l = 0
            cnt[c] += 1
            l += 1
        return ans
        
    def partitionString(self, s: str) -> int:
        ans = 1
        temp = set()
        for c in s:
            if c in temp:
                ans += 1
                temp = set()
            temp.add(c)
        return ans
        
    def partitionString(self, s: str) -> int:
        ans = 1
        mask = 0
        ord_a = ord('a')
        for c in s:
            bit = 1 << (ord(c) - ord_a)
            if mask & bit:
                ans += 1
                mask = 0
            mask |= bit
        return ans
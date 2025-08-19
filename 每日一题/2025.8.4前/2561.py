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
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = defaultdict(int)
        for num1, num2 in zip(basket1, basket2):
            cnt[num1] += 1
            cnt[num2] -= 1

        a, b = [], []
        for num, c in cnt.items():
            if c % 2 != 0:
                return -1
            if c > 0:
                a.extend([num] * (c // 2))
            else:
                b.extend([num] * (-c // 2))

        a.sort()
        b.sort(reverse=True)
        mn_temp = min(cnt)  # 中介

        return sum(min(x, y, mn_temp * 2) for x, y in zip(a, b))
    
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = defaultdict(int)
        for num1, num2 in zip(basket1, basket2):
            cnt[num1] += 1
            cnt[num2] -= 1

        a = []
        for num, c in cnt.items():
            if c % 2 != 0:
                return -1
            a.extend([num] * (abs(c) // 2))
        
        a.sort()
        mn_temp = min(cnt)
        
        return sum(min(x, mn_temp * 2) for x in a[:len(a) // 2])
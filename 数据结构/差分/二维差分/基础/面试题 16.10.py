from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
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
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        mx = ans = 0
        
        diff = [0] * 102
        for b, d in zip(birth, death):
            diff[b - 1900] += 1
            diff[d - 1900 + 1] -= 1

        pre = list(accumulate(diff))
        for i, cnt in enumerate(pre):
            if cnt > mx:
                mx = cnt
                ans = i
        return ans + 1900
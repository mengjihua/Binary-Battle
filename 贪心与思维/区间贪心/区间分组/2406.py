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
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        mx = max(end for _, end in intervals)
        diff = [0] * (mx + 2)
        for start, end in intervals:
            diff[start] += 1
            diff[end + 1] -= 1
        
        ans = 0
        for i in range(1, len(diff)):
            diff[i] += diff[i - 1]
            ans = fmax(ans, diff[i])
        return ans
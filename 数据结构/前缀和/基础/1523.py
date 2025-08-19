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
    def countOdds(self, low: int, high: int) -> int:
        cnt = ceil((high - low + 1) / 2)
        if low % 2 == 0 and high % 2 == 0:
            return cnt - 1
        return cnt
    
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2

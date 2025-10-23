from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
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
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = ''
            n = len(s)
            for i in range(n - 1):
                new_s += str((int(s[i]) + int(s[i + 1])) % 10)
            s = new_s
        return s[0] == s[1]
    
    def hasSameDigits(self, s: str) -> bool:
        n = len(s) - 2
        s = list(map(int, s))
        left, right = s[0], s[-1]

        for i in range(1, len(s) - 1):
            left = (left + comb(n, i) % 10 * s[i]) % 10
            right = (right + comb(n, i-1) % 10 * s[i]) % 10
        return left == right
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

def lower_bound(nums, target):
    cnt = 0
    l, r = 0, len(nums) - 1
    while cnt <= 32 and l <= r:
        cnt += 1
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n, m = len(spells), len(potions)
        pairs = [0] * n
        for i in range(n):
            pairs[i] = m - lower_bound(potions, success / spells[i])
        return pairs
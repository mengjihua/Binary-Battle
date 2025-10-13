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
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: (x[0], x[1]))
        ans = 0
        cover = [nums[0][0], nums[0][1]]
        
        for start, end in nums[1:]:
            if start <= cover[1] + 1:
                cover[1] = fmax(cover[1], end)
            else:
                ans += cover[1] - cover[0] + 1
                cover = [start, end]
                
        ans += cover[1] - cover[0] + 1
        return ans
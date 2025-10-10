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
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        lake_filled = defaultdict(int)
        dry_days = []
        
        for day in range(n):
            lake = rains[day]
            if lake == 0:
                dry_days.append(day)
            elif lake not in lake_filled:
                lake_filled[lake] = day
            else:
                idx = bisect_right(dry_days, lake_filled[lake])
                if idx == len(dry_days):  # 也判断了 dry_days 为空的情况
                    return []
                ans[dry_days[idx]] = lake
                lake_filled[lake] = day
                dry_days.pop(idx)  # O(n) 操作，可以用有序集合优化
                
        for day in dry_days:
            ans[day] = 1
        
        return ans
    
    # 有序集合优化
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        lake_filled = defaultdict(int)
        dry_days = SortedList()
        
        for day in range(n):
            lake = rains[day]
            if lake == 0:
                dry_days.add(day)
            elif lake not in lake_filled:
                lake_filled[lake] = day
            else:
                idx = dry_days.bisect_right(lake_filled[lake])
                if idx == len(dry_days):
                    return []
                ans[dry_days[idx]] = lake
                lake_filled[lake] = day
                dry_days.pop(idx)  # O(logn) 操作
                
        for day in dry_days:
            ans[day] = 1
        
        return ans
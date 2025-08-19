from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(target_time):
            cnt = 0
            for time in workerTimes:
                x = 2 * target_time // time
                cnt += int((-1 + sqrt(1 + 4 * x)) // 2)
            return cnt >= mountainHeight
            
        min_time = min(workerTimes)
        l, r = 0, ceil((min_time + min_time + min_time * (mountainHeight - 1)) * mountainHeight / 2)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
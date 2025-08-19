from typing import List, Tuple, Dict, Set, Optional
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
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks_cnt = Counter(ranks)
        
        def check(time):
            count = 0
            for rank, cnt in ranks_cnt.items():
                count += floor(sqrt(time / rank)) * cnt
            return count >= cars
        
        l, r = 0, min(ranks) * cars ** 2
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
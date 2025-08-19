from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        def check(x):
            return (x // a + x // b - x // lcm(a, b)) >= n

        l, r = 1, min(a, b) * n
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l % (10 ** 9 + 7)
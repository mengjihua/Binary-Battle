from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        horizon = Counter([y for _, y in points])
        pre_sum, ans = 0, 0
        for c in horizon.values():
            cnt = c * (c - 1) // 2
            ans += pre_sum * cnt
            pre_sum += cnt
        return ans % (10 ** 9 + 7)
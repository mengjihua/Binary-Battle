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
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        diff = [0] * n
        for i in range(n):
            diff[i] = capacity[i] - rocks[i]
        diff.sort()
        ans = 0
        for i in range(n):
            if diff[i] <= additionalRocks:
                ans += 1
                additionalRocks -= diff[i]
            else:
                break
        return ans
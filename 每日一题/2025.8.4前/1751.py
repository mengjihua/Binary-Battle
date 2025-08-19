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
    def maxValue(self, events: List[List[int]], k: int) -> int:
        if k == 1: return max(e[2] for e in events)
        
        events.sort(key=lambda x: x[1])
        n = len(events)
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i, (start, end, value) in enumerate(events):
            p = bisect_left(events, start, hi=i, key=lambda x: x[1])
            for j in range(1, k + 1):
                dp[i + 1][j] = max(dp[i][j], dp[p][j - 1] + value)
        return dp[n][k]
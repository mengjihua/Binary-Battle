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
    def maximumLength(self, nums: List[int], k: int) -> int:
        f = [[0] * k for _ in range(k)]
        for x in nums:
            x %= k
            for y, fxd in enumerate(f[x]):
                f[y][x] = f[x][y] + 1
        return max(map(max, f))
    
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            f = [0] * k
            for num in nums:
                num %= k
                f[num] = f[i - num] + 1
            ans = max(ans, max(f))
        return ans
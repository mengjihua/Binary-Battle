from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 6 + 1)

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans, l = 0, 0
        windows = defaultdict(int)
        for r in range(len(s)):
            while windows[s[r]] >= 2:
                windows[s[l]] -= 1
                l += 1
            windows[s[r]] += 1
            ans = max(ans, r - l + 1)
        return ans
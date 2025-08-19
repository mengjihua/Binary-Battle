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
    def numberOfSubstrings(self, s: str) -> int:
        ans, r = 0, 0
        window = defaultdict(int)
        for l in range(len(s)):
            while r < len(s) and len(window) < 3:
                window[s[r]] += 1
                r += 1
            if len(window) == 3:
                ans += len(s) - r + 1
            window[s[l]] -= 1
            if window[s[l]] == 0:
                del window[s[l]]
        return ans
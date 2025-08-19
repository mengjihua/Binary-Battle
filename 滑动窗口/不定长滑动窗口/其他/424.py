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
    def characterReplacement(self, s: str, k: int) -> int:
        ans, l = 0, 0
        window = defaultdict(int)
        max_cnt = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] > max_cnt:
                max_cnt = window[s[r]]
            while r - l + 1 - max_cnt > k:
                window[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
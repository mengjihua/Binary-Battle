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
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans, l, temp = 1, 0, 0
        window = defaultdict(int)
        window[s[0]] = 1
        for r in range(1, n):
            window[s[r]] += 1
            if s[r] == s[r - 1]: temp += 1
            while temp == 2:
                window[s[l]] -= 1
                if s[l] == s[l + 1]: temp -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
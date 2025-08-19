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
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if n < m:
            return []

        ans = []
        p_cnt = Counter(p)
        window = defaultdict(int)
        for r in range(n):
            window[s[r]] += 1
            if r < m - 1:
                continue
            if window == p_cnt:
                ans.append(r - m + 1)
            window[s[r - m + 1]] -= 1
            if window[s[r - m + 1]] == 0:
                del window[s[r - m + 1]]
        return ans
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
    def maxRepOpt1(self, text: str) -> int:
        cnt = Counter(text)
        ans, l, n = 0, 0, len(text)
        while l < n:
            j = l
            while j < n and text[j] == text[l]:
                j += 1
            r = j + 1
            while r < n and text[r] == text[l]:
                r += 1
            ans = max(ans, min(r - l, cnt[text[l]]))
            l = j
        return ans
from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans, n = 0, len(tokens)
        l, r = 0, n - 1
        while l <= r and power > 0:
            while l <= r and power >= tokens[l]:
                power -= tokens[l]
                l += 1
            ans = max(ans, l - (n - r - 1))
            while l - (n - r - 1) >= 1 and l <= r and power < tokens[l]:
                power += tokens[r]
                r -= 1
            if l < n and power < tokens[l]:
                break
        return ans
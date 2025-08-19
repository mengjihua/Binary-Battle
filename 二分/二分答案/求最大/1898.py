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
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n, m = len(s), len(p)
        
        def check(k):
            is_removable = set(removable[:k])
            j = 0
            for i in range(n):
                if i in is_removable:
                    continue
                if s[i] == p[j]:
                    j += 1
                    if j == m:
                        return True
            return False
        
        l, r = 0, len(removable)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def maxOperations(self, s: str) -> int:
        pre_one, ans = 0, 0
        judge = True
        for c in s:
            if c == '1':
                pre_one += 1
                judge = True
            elif judge:
                ans += pre_one
                judge = False
        return ans
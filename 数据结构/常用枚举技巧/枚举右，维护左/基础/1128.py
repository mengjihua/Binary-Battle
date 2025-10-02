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
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        temp = defaultdict(int)
        ans = 0
        for a, b in dominoes:
            a, b = min(a, b), max(a, b)
            ans += temp[(a, b)]
            temp[(a, b)] += 1
        return ans
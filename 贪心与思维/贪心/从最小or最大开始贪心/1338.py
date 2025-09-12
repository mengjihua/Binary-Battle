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
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        lst = sorted(cnt.values(), reverse=True)
        total = len(arr)
        cur_sum = 0
        for i, val in enumerate(lst):
            cur_sum += val
            if cur_sum >= total // 2:
                return i + 1
        return len(lst)
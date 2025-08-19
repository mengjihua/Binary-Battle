from typing import List, Tuple, Dict, Set, Optional
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
    def findLucky(self, arr: List[int]) -> int:
        arr_cnt = Counter(arr)
        ans = -1
        for val, cnt in arr_cnt.items():
            if val == cnt:
                ans = max(ans, val)
        return ans
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
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        cur_day, ans = 0, 0
        meetings.sort(key=lambda x: x[0])
        for start, end in meetings:
            if cur_day < start:
                ans += start - cur_day - 1
                cur_day = end
            else:
                cur_day = max(cur_day, end)
        return ans + days - cur_day
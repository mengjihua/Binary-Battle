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
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort(key=lambda x: x[0])
        cur_x = points[0][0]
        cnt = 1
        for x, _ in points[1:]:
            if x - cur_x > w:
                cnt += 1
                cur_x = x
        return cnt
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
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        temp = defaultdict(int)
        ans = 0
        for width, height in rectangles:
            ratio = width / height
            ans += temp[ratio]
            temp[ratio] += 1
        return ans
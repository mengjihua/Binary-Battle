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
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        temp = float('inf')
        ans, n = 0, len(maximumHeight)
        for i in range(n):
            if maximumHeight[i] < temp:
                ans += maximumHeight[i]
                temp = maximumHeight[i]
            else:
                temp -= 1
                ans += temp
            if temp <= 0:
                return -1
        return ans
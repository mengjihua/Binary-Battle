from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10 ** 5 + 1)


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        sl = SortedList()
        ans = -inf
        for i, num in enumerate(nums):
            if i >= m - 1:
                sl.add(nums[i - m + 1])

            if sl:
                mx, mn = sl[-1], sl[0]
                ans = max(ans, mx * num, mn * num)
        return ans

    def maximumProduct(self, nums: List[int], m: int) -> int:
        mx, mn = -inf, inf
        ans = -inf
        for i, num in enumerate(nums[m - 1:]):
            mx = max(mx, nums[i])
            mn = min(mn, nums[i])
            ans = max(ans, mx * num, mn * num)
        return ans
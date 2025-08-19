from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 6 + 1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n, ans, l = len(nums), float('inf'), 0
        for r in range(n):
            target -= nums[r]
            while target + nums[l] <= 0:
                target += nums[l]
                l += 1
            if target <= 0:
                ans = min(ans, r - l + 1)
        return ans if ans != float('inf') else 0
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
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, l = 0, 0
        window = defaultdict(int)
        for r in range(len(nums)):
            while window[nums[r]] >= k:
                window[nums[l]] -= 1
                l += 1
            window[nums[r]] += 1
            ans = max(ans, r - l + 1)
        return ans
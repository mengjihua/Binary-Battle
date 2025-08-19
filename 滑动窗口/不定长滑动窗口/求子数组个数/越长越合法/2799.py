from typing import List
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
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = len(set(nums))
        ans, r = 0, 0
        window = defaultdict(int)
        for l in range(len(nums)):
            while r < len(nums) and len(window) < cnt:
                window[nums[r]] += 1
                r += 1
            if len(window) == cnt:
                ans += len(nums) - r + 1
            window[nums[l]] -= 1
            if window[nums[l]] == 0:
                del window[nums[l]]
        return ans
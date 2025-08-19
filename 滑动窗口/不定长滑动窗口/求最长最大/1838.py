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
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, temp, ans = 0, 0, 0
        for r in range(len(nums)):
            temp += nums[r]
            while nums[r] * (r - l + 1) - temp > k:
                temp -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
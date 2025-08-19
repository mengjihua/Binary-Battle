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
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(0) == 0:
            return len(nums) - 1
        
        ans, l = 0, 0
        window = defaultdict(int)
        for r in range(len(nums)):
            while nums[r] == 0 and window[0] >= 1:
                window[nums[l]] -= 1
                l += 1
            window[nums[r]] += 1
            ans = max(ans, window[1])
        return ans
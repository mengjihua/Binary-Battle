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
    # def findLHS(self, nums: List[int]) -> int:
    #     nums.sort()
    #     n = len(nums)
    #     ans, l, r = 0, 0, 0
    #     while r < len(nums) - 1:
    #         while r + 1 < n and nums[r + 1] - nums[l] <= 1:
    #             r += 1
    #         ans = max(ans, r - l + 1) if nums[r] - nums[l] == 1 else ans
    #         l += 1
    #     return ans
    
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for num, cnt in count.items():
            if num + 1 in count:
                ans = max(ans, cnt + count[num + 1])
        return ans
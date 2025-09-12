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
    # def maximizeGreatness(self, nums: List[int]) -> int:
    #     nums.sort()
    #     ans = 0
    #     # r = 0
    #     # for l in range(len(nums)):
    #     #     while r < len(nums) and nums[r] <= nums[l]:
    #     #         r += 1
    #     #     if r < len(nums) and nums[r] > nums[l]:
    #     #         ans += 1
    #     #         r += 1
    #     # return ans
    #     l = 0
    #     for num in nums:
    #         if num > nums[l]:
    #             l += 1
    #     return l
    
    def maximizeGreatness(self, nums: List[int]) -> int:
        return len(nums) - max(Counter(nums).values())
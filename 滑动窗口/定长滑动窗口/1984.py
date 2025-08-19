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
    # def minimumDifference(self, nums: List[int], k: int) -> int:
    #     n = len(nums)
    #     nums.sort()
    #     return min(nums[i + k - 1] - nums[i] for i in range(n - k + 1))
    
    def minimumDifference(self, nums: List[int], k: int) -> int:
        return min(i - j for i, j in zip(sorted(nums)[k - 1:], sorted(nums)[:-k + 1])) if k != 1 else 0
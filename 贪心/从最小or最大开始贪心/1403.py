from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort(reverse=True)
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum > total - cur_sum:
                return nums[:i + 1]
        return nums
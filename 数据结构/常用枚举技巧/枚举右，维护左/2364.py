from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for idx, num in enumerate(nums):
            count[num - idx] += 1
        total_pairs = len(nums) * (len(nums) - 1) // 2
        good_pairs = sum(c * (c - 1) // 2 for c in count.values())
        return total_pairs - good_pairs
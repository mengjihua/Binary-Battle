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
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans, l, temp = 0, 0, 0
        window = defaultdict(int)
        for r in range(len(nums)):
            window[nums[r]] += 1
            temp += nums[r]
            while window[nums[r]] > 1:
                window[nums[l]] -= 1
                temp -= nums[l]
                l += 1
            ans = max(ans, temp)
        return ans
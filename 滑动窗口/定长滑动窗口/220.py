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


# TODO: 桶做法
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = defaultdict(int)
        
        for r, num in enumerate(nums):
            window[num] += 1
            if window[num - 1] or window[num + 1]:
                return True
            
            l = r - indexDiff
            if l < 0:
                continue
            
            window[nums[l]] -= 1
            if window[nums[l]] == 0:
                del window[nums[l]]
                
        return False
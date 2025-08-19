from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10 ** 5 + 1)
def _max(a, b):
    return a if a > b else b

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf_max = [0] * n
        suf_max[-1] = nums[-1]
        for i in range(n - 2, 1, -1):
            suf_max[i] = _max(suf_max[i + 1], nums[i])
        
        ans, pre_max = 0, nums[0]
        for i in range(1, n - 1):
            ans = _max(ans, (pre_max - nums[i]) * suf_max[i + 1])
            pre_max = _max(pre_max, nums[i])
        return ans
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_num = _max(nums[0], nums[1])
        diff_max = nums[0] - nums[1]
        ans = 0
        for i in range(2, len(nums)):
            ans = _max(ans, diff_max * nums[i])
            diff_max = _max(diff_max, max_num - nums[i])
            max_num = _max(max_num, nums[i])
        return ans
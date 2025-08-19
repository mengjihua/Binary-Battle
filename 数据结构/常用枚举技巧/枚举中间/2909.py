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

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        pre_min, suf_min = [0] * len(nums), [0] * len(nums)
        
        pre_min[0] = nums[0]
        for i in range(1, len(nums)):
            pre_min[i] = min(pre_min[i - 1], nums[i])
            
        suf_min[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])
            
        ans = inf
        for i in range(1, len(nums) - 1):
            l_min,  r_min = pre_min[i - 1], suf_min[i + 1]
            if l_min < nums[i] > r_min:
                ans = min(ans, l_min + r_min + nums[i])
        return ans if ans != inf else -1
    
    def minimumSum(self, nums: List[int]) -> int:
        suf_min = [0] * len(nums)
        suf_min[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])
                        
        ans = pre_min = inf
        for i in range(len(nums) - 1):
            if pre_min < nums[i] > suf_min[i + 1]:
                ans = min(ans, pre_min + suf_min[i + 1] + nums[i])
            pre_min = min(pre_min, nums[i])
                
        return ans if ans != inf else -1
        
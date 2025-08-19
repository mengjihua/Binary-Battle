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
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_lst = defaultdict(list)
        for i, num in enumerate(nums):
            pos_lst[num].append(i)
        
        ans = 0
        for idx_lst in pos_lst.values():
            if len(idx_lst) <= ans:
                continue
            l = 0
            for r in range(len(idx_lst)):
                while idx_lst[r] - idx_lst[l] + 1 - (r - l + 1) > k:
                    l += 1
                ans = max(ans, r - l + 1)
        return ans
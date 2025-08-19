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
    def getLargestOutlier(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        total = sum(nums)

        ans = -inf
        for num in nums:
            cnt[num] -= 1
            if (total - num) % 2 == 0 and cnt[(total - num) // 2] > 0:
                ans = max(ans, num)
            cnt[num] += 1
        return ans
    
    
    def getLargestOutlier(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        total = sum(nums)

        ans = -inf
        for num in nums:
            cnt[num] -= 1
            if cnt[total - num * 2] > 0:
                ans = max(ans, total - num * 2)
            cnt[num] += 1
        return ans
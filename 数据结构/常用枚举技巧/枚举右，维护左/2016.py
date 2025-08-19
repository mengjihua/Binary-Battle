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
    def maximumDifference(self, nums: List[int]) -> int:
        n, min_num, ans = len(nums), nums[0], -1
        for i in range(1, n):
            ans = max(ans, nums[i] - min_num)
            min_num = min(min_num, nums[i])
        return ans if ans != 0 else -1
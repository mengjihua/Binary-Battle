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
    def countNicePairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        
        def rev(num):
            return int(str(num)[::-1])
        
        ans = 0
        for num in nums:
            rev_num = rev(num)
            ans += cnt[num - rev_num]
            cnt[num - rev_num] += 1
        return ans % (10 ** 9 + 7)
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
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        temp = defaultdict(int)
        
        def get_sum(num):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res
        
        for num in nums:
            sum_digit = get_sum(num)
            if sum_digit in temp:
                ans = max(ans, temp[sum_digit] + num)
            temp[sum_digit] = num
        return ans
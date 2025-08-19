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
    # def maxSum(self, nums: List[int]) -> int:
    #     temp = defaultdict(int)
    #     ans = 0
        
    #     def get_max_digit(num: int) -> int:
    #         res = 0
    #         while num > 0:
    #             res = max(res, num % 10)
    #             num //= 10
    #         return res
        
    #     for num in nums:
    #         max_digit = get_max_digit(num)
    #         if max_digit in temp:
    #             ans = max(ans, temp[max_digit] + num)
    #         temp[max_digit] = max(temp[max_digit], num)
    #     return ans if ans > 0 else -1
    
    def maxSum(self, nums: List[int]) -> int:
        temp = [-inf] * 10
        ans = -1
        
        def get_max_digit(num: int) -> int:
            res = 0
            while num > 0:
                res = max(res, num % 10)
                num //= 10
            return res
        
        for num in nums:
            max_digit = get_max_digit(num)
            ans = max(ans, temp[max_digit] + num)
            temp[max_digit] = max(temp[max_digit], num)
        return ans if ans > 0 else -1